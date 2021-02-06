import numpy as np


class LinearRegressionMBGD:
    """ 线性回归问题的小批量梯度下降算法 """
    def fit(self, X, y, eta_0=10, eta_1=50, N=3000, B=10):
        """ 模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1))
        self.w = np.zeros((n, 1))
        for t in range(N):
            batch = np.random.randint(low=0, high=m, size=B)        # 随机选择 B条训练数据
            X_batch = X[batch].reshape(B, -1)
            y_batch = y[batch].reshape(B, -1)
            e = X_batch.dot(cw) - y_batch
            g = 2* X_batch.T.dot(e) / B                             # 计算由这 B条数据形成的梯度
            eta_t = eta_0 / (eta_1 + t)                             # 计算步长
            cw -= eta_t* g                                          # 移动
            self.w += cw                                            # 求和以求平均
        self.w /= N

    def predict(self, X):
        """ 预测函数 """
        return X.dot(self.w)
# end
