import numpy as np

class Hubber_SubGD:
    """ 鲁棒回归算法的次梯度下降方法实现 """
    def __init__(self, epsilon=0.5):
        """ 初始化 Hubber损失函数的参数 """
        self.epsilon = epsilon

    def data_split(self, X, y, abs_error):
        """ 按照epslion分割数据 """
        m, n = X.shape
        X_out, y_out = np.empty(shape=(0, n)), np.empty(shape=(0, 1))
        X_inn, y_inn = np.empty(shape=(0, n)), np.empty(shape=(0, 1))
        for i in range(m):
            if abs_error[i] > self.epsilon:
                X_out = np.append(X_out, X[i].reshape((1, -1)), axis=0)
                y_out = np.append(y_out, y[i].reshape((1, -1)), axis=0)
            else:
                X_inn = np.append(X_inn, X[i].reshape((1, -1)), axis=0)
                y_inn = np.append(y_inn, y[i].reshape((1, -1)), axis=0)
        return X_out, y_out, X_inn, y_inn

    def fit(self, X, y, eta=0.1, N=1000):
        """ 训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1)).reshape(-1, 1)                   # 当前位置
        self.w = np.zeros((n, 1)).reshape(-1, 1)
        for i in range(N):
            allerror = X.dot(cw) - y                       # m* 1
            abs_allerror = abs(allerror)
            X_out, y_out, X_inn, y_inn = self.data_split(X, y, abs_allerror)
            inn_m, inn_n = X_inn.shape
            out_m, out_n = X_out.shape
            innerror = X_inn.dot(cw) - y_inn
            inn_v = (2* X_inn.T.dot(innerror) / inn_m)
            cw -= eta* inn_v
            # print("inn_v: {}".format(inn_v))

            outerror = (X_out.dot(cw) - y_out)
            # norms = np.linalg.norm(outerror, 1, axis=0).reshape(1, -1)
            # exterror = (2* self.epsilon / out_m)* norms + self.epsilon**2

            sumd = np.zeros((n, 1)).reshape(-1, 1)
            for j in range(out_m):                          # 此处实际上可以使用向量对矩阵 X_out进行求和，尽量减少此类矩阵迭代
                if outerror[j] > 0:
                    sumd = np.add(sumd, X_out[j, :].reshape(-1, 1))
                elif outerror[j] < 0:
                    sumd = np.add(sumd, -1.0* X_out[j, :].reshape(-1, 1))

            sumd *= (2* self.epsilon / out_m)
            # print("sumd: {}".format(sumd))
            cw -= eta* sumd

            self.w += cw
        self.w /= N

    def predict(self, X):
        """ 预测函数 """
        return X.dot(self.w.reshape(-1, 1))
