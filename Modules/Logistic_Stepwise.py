import numpy as np
from scipy.stats import f


def sigmoid(scores):
    """ Sigmoid函数的实现 """
    return 1.0 / (1.0 + np.exp(-scores))

class LogisticStepwise:
    """ Logistic & SGD & 向前逐步回归算法 """
    def fit(self, X, y, eta_0=10, eta_1=50, N=20000):
        """ 模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1))
        self.w = np.zeros((n, 1))
        for t in range(N):
            i = np.random.randint(m)
            x = X[i].reshape(1, -1)
            pred = sigmoid(x.dot(cw))
            g = x.T* (pred - y[i])
            cw -= (eta_0 / (t + eta_1))* g
            self.w += cw
        self.w /= N
        return self.w

    def f_test(self, mse_A, mse_min, m):
        """F检验"""
        if mse_min > mse_A:
            return False
        F = mse_A / mse_min
        p_value = f.cdf(F, m, m)                             # 通过 F分布的累计分布函数来计算置信度
        return (p_value > 0.95)                              # 若置信度大于 0.95 ，则返回 True

    def forward_selection(self, X, y, eta_0=10, eta_1=50, N=20000):
        """向前特征选择函数"""
        m, n = X.shape
        A, C = [0], [i for i in range(1, n)]
        while len(C) > 0:
            self.fit(X[:, A], y, eta_0, eta_1, N)
            proba = sigmoid(X[:, A].dot(self.w))
            CE_A = self.cross_entropy(y, proba)             # 计算现有选中特征下的 mse
            CE_min, j_min = float("inf"), -1                # 寻找再加一个特征之后，模型的最小 mse
            for j in C:
                self.fit(X[:,  A + [j]], y, eta_0, eta_1, N)
                proba_j = sigmoid(X[:, A + [j]].dot(self.w))
                CE_j = self.cross_entropy(y, proba_j)             # 计算现有选中特征下的 mse
                if CE_j < CE_min:
                    CE_min, j_min = CE_j, j
            if self.f_test(CE_A, CE_min, m):               # 如果这个新模型的 mse 通过了 f检测，就接受它
                A.append(j_min)
                C.remove(j_min)
            else:
                break                                        # 这些剩下的特征一个有用的都没有，就不再选了
        self.fit(X[:, A], y)                                 # 最终采用数据中的这些特征去训练模型，并记录 w
        self.A = A                                           # 记录选出来的这些特征

    def predict_proba(self, X):
        """ 完成概率预测任务 """
        return sigmoid(X[:, self.A].dot(self.w))

    def predict(self, X):
        """ 完成类别预测任务 """
        proba = self.predict_proba(X)
        return (proba >= 0.7).astype(np.int)        # 使用了阈值为 0.7的阈值分类函数（或者说最大概率分类函数）

    def cross_entropy(self, y_true, y_pred):        # 注意类内方法第一个参数必须是 self
        """ 交叉熵函数 """
        return np.average((-y_true* np.log(y_pred)) - ((1 - y_true)* np.log(1 - y_pred)))
# end


# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html
# https://baike.baidu.com/item/F%E5%88%86%E5%B8%83/7917090
# https://www.zhihu.com/question/308849589
