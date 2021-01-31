import numpy as np

class RidgeRegression:
    """岭回归模型类"""
    def __init__(self, Lambda=0.01):
        """初始化正则化系数"""
        self.Lambda = Lambda                            
    # end

    def fit(self, X, y):
        """模型训练函数"""
        m, n = X.shape
        r = m* np.diag(self.Lambda* np.ones(n))         # ** 这里与参考书一致，官方代码库没有乘以 m **
        self.w = np.linalg.inv(X.T.dot(X) + r).dot(X.T).dot(y)
    # end

    def predict(self, X):
        """模型预测函数"""
        return X.dot(self.w)
    # end
# end
        