import numpy as np


def softmax_single(scores):
    """ Softmax函数（单数据，输入向量，输出向量） """
    e = np.exp(scores)
    s = e.sum()
    for i in range(len(e)):
        e[i] /= s
    return e
# end

def softmax_multi(scores):
    """ Softmax函数（多数据，输入矩阵，输出矩阵） """
    e = np.exp(scores)
    s = e.sum(axis=1)       # exp(<xi, w1>) + ... + exp(<xi, wk>), i∈[1, m]
    for i in range(len(s)):
        e[i] /= s[i]
    return e
# end

class SoftmaxRegressionSGD:
    """ Softmax回归算法 """
    def fit(self, X, Y, eta_0=50, eta_1=100, N=5000):
        """ 训练函数 """
        m, n = X.shape
        m, k = Y.shape
        CW = np.zeros(n* k).reshape(n, k)
        self.W = np.zeros(n* k).reshape(n, k)
        for t in range(N):
            i = np.random.randint(m)
            x = X[i].reshape(1, -1)                    # 行向量
            proba = softmax_single(x.dot(CW))          # 注意这里只应计算一条数据的预测值
            g = x.T.dot(proba - Y[i])
            CW -= (eta_0 / (t + eta_1))* g
            self.W += CW
        self.W /= N

    def predict_proba(self, X):
        """ 概率预测函数 """
        return softmax_multi(X.dot(self.W))

    def predict(self, X):
        """ 类别预测函数 """
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)
# end
