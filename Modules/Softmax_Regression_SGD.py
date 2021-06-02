import numpy as np


def softmax_single(scores):    # scores: (<x[i], w1>, <x[i], w2>, ..., <x[i], wk>)
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
    s = e.sum(axis=1)          # col(m by 1): (exp(sum<x1, w1~k>) , ... , exp(sum<xm, w1~k>))
    for i in range(len(s)):
        e[i] /= s[i]           # erow_i's elements divide s[i]
    return e
# end

class SoftmaxRegressionSGD:
    """ Softmax回归算法 """
    def fit(self, X, Y, eta_0=50, eta_1=100, N=5000):
        """ 训练函数 """
        m, n = X.shape
        m, k = Y.shape
        CW = np.zeros(n* k).reshape(n, k)              # W = (w1, w2, ..., wk), wi: n by 1
        self.W = np.zeros(n* k).reshape(n, k)
        for t in range(N):
            i = np.random.randint(m)
            x = X[i].reshape(1, -1)                    # 行向量
            proba = softmax_single(x.dot(CW))          # 注意这里只应计算一条数据属于各类的预测概率向量 (SGD)
            g = x.T.dot(proba - Y[i])                  # colv dot rowv --> matrix
            CW -= (eta_0 / (t + eta_1))* g
            self.W += CW
        self.W /= N

    def predict_proba(self, X):
        """ 概率预测函数 """
        return softmax_multi(X.dot(self.W))

    def predict(self, X):
        """ 类别预测函数 """
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)                 # 按照最大概率分类原则，直接返回每条数据对应的数值型预测标签（非 one-hot向量标签）
# end
