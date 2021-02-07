import numpy as np


class LinearRegressionGD:
    """ 线性回归类的梯度下降实现 """
    def fit(self, X, y, eta, N):
        """ 训练函数 (eta : 训练步长 | N : 迭代次数) """
        m, n = X.shape
        w = np.zeros((n, 1))
        for t in range(N):
            e = X.dot(w) - y                # 计算经验损失
            g = 2* X.T.dot(e) / m           # 计算梯度 (均方误差函数在该点之梯度，'g' for "Gradient")
            w -= eta* g                     # 更新特征参数（向着梯度的反方向移动：步长* 梯度）
        self.w = w

    def predict(self, X):
        """ 线性模型的预测函数 """
        return X.dot(self.w)
# end
