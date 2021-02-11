import numpy as np


def sigmoid(scores):
    """ Sigmoid函数的实现 """
    return 1.0 / (1.0 + np.exp(-scores))
# end

class LogisticRegressionSGD:
    """ Logistic回归的随机梯度下降优化算法 """
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

    def predict_proba(self, X):
        """ 完成概率预测任务 """
        return sigmoid(X.dot(self.w))

    def predict(self, X):
        """ 完成类别预测任务 """
        proba = self.predict_proba(X)
        return (proba >= 0.5).astype(np.int)        # 使用了阈值为 0.5的阈值分类函数（或者说最大概率分类函数）

    def cross_entropy(self, y_true, y_pred):        # 注意类内方法第一个参数必须是 self
        """ 交叉熵函数 """
        return np.average((-y_true* np.log(y_pred)) - ((1 - y_true)* np.log(1 - y_pred)))
# end
