import numpy as np


class LinearRegression:
    """线性回归的正规方程算法"""
    def fit(self, X, y):
        """模型训练成员函数"""
        self.w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)          # 存储模型参量：w = inv(X.T·X)·(X.T)·y

    def predict(self, X):
        """模型预测成员函数（各特征的线性组合）"""
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
