from ast import Lambda
import numpy as np

class SVM_SMO:
    """ 支持向量机的SMO算法实现 """
    def get_H(self, Lambda, i, j, y):
        """ 计算Lambda[j]的上限 """
        if y[i] == y[j]:
            return Lambda[i] + Lambda[j]
        else:
            return float("inf")
    # end

    def get_L(self, Lambda, i, j, y):
        """ 计算Lambda[j]的下限 """
        if y[i] == y[j]:
            return 0.0
        else:
            return max(0.0, Lambda[j] - Lambda[i])
    # end

    def smo(self, X, y, K, N):
        """ SMO算法实现主体 """
        m, n = X.shape
        y = y.reshape(m,)                           # 确保 y为 ndarray类型，下面要用 np.multiply 做 hadamard product（不可以用 np.array！）
        Lambda = np.zeros(m)                        # 初始化 Lambda的值（为 ndarray类型）
        epsilon = 1e-8                              # 设定计算 0值，计算值小于此数视为 0
        for r in range(N):
            for i in range(m):
                for j in range(m):
                    D_ij = 2* K[i][j] - K[i][i] - K[j][j]
                    if abs(D_ij) < epsilon:
                        continue
                    E_i = np.array(K[:, i]).dot(np.multiply(Lambda, y)) - y[i]    
                    E_j = np.array(K[:, j]).dot(np.multiply(Lambda, y)) - y[j]
                    fraction = (E_j - E_i) / D_ij                                 # 算式内层的分数
                    NSL_j = Lambda[j] + fraction* y[j]                            # 计算新的 Lambda[j]（还未限界）
                    H_ij = self.get_H(Lambda, i, j, y)                            # 获得新 Lambda[j]的上界
                    L_ij = self.get_L(Lambda, i, j, y)
                    delta_j = max(L_ij, min(NSL_j, H_ij)) - Lambda[j]
                    Lambda[j] += delta_j
                    Lambda[i] -= y[i]* y[j]* delta_j                              # 更新选定的两个 Lambda分量的值
                    if Lambda[i] > epsilon:                                       # 计算并存储 b
                        self.b = y[i] - np.array(K[:, i]).dot(np.multiply(Lambda, y))
                    elif Lambda[j] > epsilon:
                        self.b = y[j] - np.array(K[:, j]).dot(np.multiply(Lambda, y))
        self.Lambda = Lambda                                                      # 存储 Lambda的最终结果
        self.w = np.dot(X.T, np.multiply(self.Lambda, y))                         # 计算并存储 w的值
    # end

    def fit(self, X, y, N=10):
        """ 训练函数 """
        K = np.dot(X, X.T)                                                        # 计算内积矩阵，K[i][j] = <X[i], X[j]>, K[i][j] = K[j][i]
        self.smo(X, y, K, N)
    # end

    def predict(self, X):
        """ 预测函数 """
        return np.sign(np.dot(X, self.w) + self.b)
    # end

    def predict_confidence(self, X):
        """ 根据所有样本到分离直线的距离之和作为算法的类别置信度 """
        m, n = X.shape
        vector_w = self.w.reshape(-1, 1)
        array_w = self.w.reshape(n,)
        numerator = abs(np.dot(X, vector_w) + self.b)               # 注意：是向量
        denominator = np.linalg.norm(array_w, ord=2)
        return (numerator / denominator)                            # 返回一个向量，即每个样本都有自己的置信度
    # end



# The * operator can be used as a shorthand for np.multiply on ndarrays.
# https://blog.csdn.net/prostarmoon/article/details/85261548
# https://stackoverflow.com/questions/40034993/how-to-get-element-wise-matrix-multiplication-hadamard-product-in-numpy
# https://numpy.org/doc/stable/reference/generated/numpy.multiply.html
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
# https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
