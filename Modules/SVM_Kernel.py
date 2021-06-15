import numpy as np
from SVM_SMO import SVM_SMO


class SVM_Kernel(SVM_SMO):
    """ 使用核方法的硬间隔支持向量机算法 """
    def __init__(self, kernel=None):
        """ 主要是初始化核函数对象 """
        super().__init__()
        self.kernel = kernel
    # end

    def get_K(self, X_1, X_2):
        """ 获得投影内积矩阵 """
        if self.kernel is None:
            return np.dot(X_1, X_2.T)                            # 若未指定任何核函数，算法退化成普通 SMO算法
        m1, n1 = X_1.shape
        m2, n2 = X_2.shape
        K = np.zeros((m1, m2))
        for i in range(m1):
            for j in range(m2):
                K[i][j] = self.kernel(X_1[i], X_2[j])            # 选中两个训练样本作为输入，将核函数的两个参数看作向量
        return K
    # end

    def fit(self, X, y, N=10):
        K = self.get_K(X, X)
        self.smo(X, y, K, N)
        self.X_train = X                                         # 模型输出需要用到训练数据的信息
        self.y_train = y
    # end

    def predict(self, X):
        K = self.get_K(X, self.X_train)
        return np.sign(np.dot(K, np.multiply(self.Lambda, self.y_train)) + self.b)
    # end
