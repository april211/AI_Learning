import numpy as np


class LinearRegressionSGD:
    """ 线性回归问题的随机梯度下降算法 """
    def fit(self, X, y, eta_0=10, eta_1=50, N=3000):
        """ 训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1)).reshape(-1, 1)
        self.w = np.zeros((n, 1)).reshape(-1, 1)
        for t in range(N):
            i = np.random.randint(m)                    # 随机选取一条训练数据：[0, m)
            x = X[i].reshape(1, -1)                     # 行向量
            e = x.dot(cw) - y[i]
            g = 2* e* x.T                               # 列向量（要与 w 相减）
            eta_t = eta_0 / (eta_1 + t)                 # 计算本次迭代的学习速率
            cw -= eta_t* g                              # 更新模型参数 -= 学习速率* 梯度
            self.w += cw                                # 准备求平均值
        self.w /= N

    def predict(self, X):
        """ 预测函数 """
        return X.dot(self.w)
# end
