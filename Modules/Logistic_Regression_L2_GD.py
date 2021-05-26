import numpy as np


def sigmoid(scores):
    """ Sigmoid函数的实现 """
    return 1.0 / (1.0 + np.exp(-scores))
# end

class LogisticRegressionL2GD:
    """ Logistic回归的L2正则化&梯度下降优化算法 """
    def __init__(self, Lambda=0.1):
        """ 初始化正则化强度参数 """
        self.Lambda = Lambda
    
    def fit(self, X, y, eta=0.1, N=1000):
        """ 模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1)).reshape(-1, 1)
        for t in range(N):
            h = sigmoid(X.dot(cw))
            g = (1.0 / m)* (X.T.dot(h - y)) + (2* self.Lambda* cw)
            cw -= eta* g
        self.w = cw

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
