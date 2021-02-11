import numpy as np


def softmax(scores):
    """ Softmax函数（多数据） """
    e = np.exp(scores)
    s = e.sum(axis=1)       # exp(<xi, w1>) + ... + exp(<xi, wk>), i∈[1, m]
    for i in range(len(s)):
        e[i] /= s[i]
    return e
# end

class SoftmaxRegressionGD:
    """ Softmax回归算法 """
    def fit(self, X, Y, eta=0.1, N=5000):
        """ 训练函数 """
        m, n = X.shape
        m, k = Y.shape
        CW = np.zeros(n* k).reshape(n, k)
        for t in range(N):
            proba = softmax(X.dot(CW))
            g = (1.0 / m)* X.T.dot(proba - Y)
            CW -= eta* g
        self.W = CW

    def predict_proba(self, X):
        """ 概率预测函数 """
        return softmax(X.dot(self.W))

    def predict(self, X):
        """ 类别预测函数 """
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)
# end
