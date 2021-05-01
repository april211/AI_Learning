import numpy as np
from scipy.stats import f
import copy


class StepwiseRegressionBW:
    """向后逐步回归算法类（贪心）"""
    def fit(self, X, y):
        """训练函数"""
        return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)     # 优化目标：最小均方误差（暂时先不用记录 w）

    def compute_mse(self, X, y):
        """计算均方误差"""
        w = self.fit(X, y)
        r = y - X.dot(w)
        return r.T.dot(r)

    def f_test(self, mse_A, mse_min, m):
        """F检验"""
        F = mse_min / mse_A                                 # F > 1
        p_value = f.cdf(F, m, m)                            # 通过 F分布的累计分布函数来计算置信度
        # print("p_value: {}".format(p_value))
        return (p_value < 0.95)                   # 若置信度（显著性水平）小于 0.95，说明该特征不能显著降低均方误差

    def backward_selection(self, X, y):
        """向后特征选择函数"""
        m, n = X.shape
        A = [i for i in range(0, n)]
        while len(A) > 1:
            MSE_A = self.compute_mse(X[:, A], y)       # 计算现有选中特征下的 mse
            MSE_min, j_min = float("inf"), -1          # 寻找再加一个特征之后，模型的最小 mse
            for j in A:
                C = copy.deepcopy(A)
                C.remove(j)
                MSE_j = self.compute_mse(X[:, C], y)
                if MSE_j < MSE_min:
                    MSE_min, j_min = MSE_j, j
            if self.f_test(MSE_A, MSE_min, m):               # 如果这个新模型的 mse 通过了 f检测，就接受它
                A.remove(j_min)
            else:
                break                                        # 这些剩下的特征一个有用的都没有，就不再选了
        self.w = self.fit(X[:, A], y)                        # 最终采用数据中的这些特征去训练模型，并记录 w
        self.A = A                                           # 记录选出来的这些特征

    def predict(self, X):
        """预测函数"""
        return X[:, self.A].dot(self.w)                      # 预测的时候，就用选出来的这些特征去预测（X是原始数据）
# end


# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html
# # https://zhuanlan.zhihu.com/p/139151375
# https://baike.baidu.com/item/F%E5%88%86%E5%B8%83/7917090
# https://www.zhihu.com/question/308849589
