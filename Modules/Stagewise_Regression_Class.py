import numpy as np


class StagewiseRegression:
    "特征选择算法：分段回归"
    def feature_selection(self, X, y, N, eta):
        """ 特征选择函数 (N : 迭代次数 | eta : 学习步长) ，完成了模型训练的任务"""
        m, n = X.shape
        norms = np.linalg.norm(X, 2, axis=0).reshape(-1, 1)    # 求 X矩阵各列向量的 L2范数，构成 (n by 1)列向量
        w = np.zeros(n).reshape(-1, 1)
        t = 0                                          # 计数器
        r = y                                          # 这实际上是 r的初始值 (w == 0)，这样写可简化计算
        while t < N:
            c = X.T.dot(r) / norms                     # 计算相关系数（为简化运算，不除以由 r的L2范数 构成的矩阵）
            j_max = np.argmax(abs(c))                  # 找出相关系数矩阵中绝对值最小的列
            delta = eta* np.sign(c[j_max])             # 计算 对应特征参数变化量 == 学习步长* (1 | 0 | -1)
            w[j_max] += delta                          # w列向量对应的分量（刚找出的）增加（可以理解为权值增大）
            r -= delta* X[:, j_max].reshape(-1, 1)     # 更新 r列向量（以 X的列向量的线性组合去理解会方便许多）
            t += 1                                     # 迭代次数 +1
        self.w = w                                     # 记录模型参数列向量
        return w

    def predict(self, X):
        """ 预测函数 """
        return X.dot(self.w)
# end


# https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
