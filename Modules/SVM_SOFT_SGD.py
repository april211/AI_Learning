import numpy as np


class SoftSVM:
    """ 使用Hinge损失的软间隔支持向量机的随机梯度下降算法实现 """
    def __init__(self, C=1000) -> None:
        self.C = C
    # end

    def fit(self, X, y, eta=0.01, N=5000):
        """ 训练函数 """
        m, n = X.shape
        cw, cb = np.zeros((n, 1)), 0
        self.w, self.b = np.zeros((n, 1)), 0
        for r in range(N):
            ri = np.random.randint(m)
            rx = X[ri].reshape(-1, 1)
            ry = y[ri]
            s = (np.dot(cw.T, rx) + cb)* ry
            e = (s < 1).astype(np.int64)
            g_w = -e* ry* rx + (1.0 / self.C)* cw
            g_b = -e* ry
            cw -= eta* g_w
            cb -= eta* g_b
            self.w += cw
            self.b += cb
        self.w /= N
        self.b /= N
    # end

    def predict(self, X):
        """ 预测函数 """
        return np.sign(X.dot(self.w) + self.b)
    # end
# end
