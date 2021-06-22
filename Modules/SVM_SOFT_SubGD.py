import numpy as np


class SoftSVM:
    """ 使用Hinge损失的软间隔支持向量机的次梯度下降算法实现 """
    def __init__(self, C=1000) -> None:
        self.C = C
    # end

    def fit(self, X, y, eta=0.01, N=5000):
        """ 训练函数 """
        m, n = X.shape
        w, b = np.zeros((n, 1)), 0
        for r in range(N):
            s = (X.dot(w) + b)* y
            e = (s < 1).astype(np.int64).reshape(-1, 1)
            g_w = (-1/m)* X.T.dot(y* e) + (w / (m* self.C))
            g_b = (-1/m)* (y* e).sum()
            w = w - eta* g_w
            b = b - eta* g_b
        self.w = w
        self.b = b
    # end

    def predict(self, X):
        return np.sign(X.dot(self.w) + self.b)
    # end
# end
