import numpy as np

class RidgeRegression:
    """岭回归模型类"""
    def __init__(self, Lambda=0.01):
        """初始化正则化系数"""
        self.Lambda = Lambda           

    def fit(self, X, y):
        """模型训练函数"""
        m, n = X.shape
        r = m* np.diag(self.Lambda* np.ones(n))         # ** 这里改为与参考书版本一致，官方代码库没有乘以 m **
        self.w = np.linalg.inv(X.T.dot(X) + r).dot(X.T).dot(y)

    def predict(self, X):
        """模型预测函数"""
        return X.dot(self.w)

    def mean_squared_error(self, y_true, y_pred):
        """均方误差评估函数"""
        return np.average((y_true - y_pred)**2, axis=0)

    def r2_score(self, y_true, y_pred):
        """决定系数评估函数"""
        numerator = (y_true - y_pred)**2
        denumerator = (y_true - np.average(y_true, axis=0))**2
        return 1-(numerator.sum(axis=0)/denumerator.sum(axis=0))
# end
