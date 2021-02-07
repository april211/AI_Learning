import numpy as np


class Lasso:
    """ Lasso模型的坐标下降法实现 """
    def __init__(self, Lambda=1):
        self.Lambda = Lambda

    def soft_threshold(self, t, x):
        """ 柔和阈值函数实现 """
        if x > t:                       # x > t
            return x - t
        elif x >= -t:                   # x∈ [-t, t]
            return 0
        else:                           # x < -t
            return x + t

    def fit(self, X, y, N=1000):
        """ 训练函数 """
        m, n = X.shape
        alpha = (2 / m)* np.sum(X**2, axis = 0)         # 一阶导函数里的这个部分是可以提前全部算出来的
        cw = np.zeros((n, 1)).reshape(-1, 1)
        for t in range(N):
            j = t % n                           # 选出一个特征分量
            cw[j] = 0                            # 这里强调：w[j] 不是一个累积量，每次需要重新计算（单变量最优值）
            e_j = X.dot(cw.reshape(-1, 1)) - y   # 去除分量 j 后的剩余分量的 “误差”，每次迭代都需要重新计算
            beta_j = 2* X[:, j].dot(e_j) / m    # 导函数的另一部分，每次迭代也需要重新计算
            cw[j] = self.soft_threshold(self.Lambda / alpha[j], -beta_j / alpha[j])   # 求解一个单变量凸优化问题
        self.w = cw                              # 迭代完成，得到最终答案

    def predict(self, X):
        """ 预测函数 """
        return X.dot(self.w.reshape(-1, 1))
# end
