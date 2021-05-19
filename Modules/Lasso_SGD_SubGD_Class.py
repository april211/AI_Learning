import numpy as np
import Classification_Metrics as cm

class Lasso:
    """ Lasso回归问题的 随机梯度下降算法 + 次梯度 解决方案 """
    def __init__(self, Lambda=1):
        """ 初始化正则化强度超参数 """
        self.Lambda = Lambda

    def fit(self, X, y, eta_0=10, eta_1=50, N=6000):
        """ Lasso线性模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1)).reshape(-1, 1)                   # 当前位置
        self.w = np.zeros((n, 1)).reshape(-1, 1)
        loss = np.array([])
        for t in range(N):
            i = np.random.randint(m)                    # 随机选择 1条训练数据
            x = X[i].reshape(1, -1)                     # 行向量
            eta_t = eta_0 / (eta_1 + t)                 # 计算学习速率
            e = x.dot(cw) - y[i]
            v = 2* e* x.T + (self.Lambda* np.sign(cw))  # 使用了次梯度的概念（选择了一个）
            cw -= eta_t* v
            closs = cm.mean_squared_error(y, X.dot(cw))             # 记录决定系数
            loss = np.append(loss, closs)                     # 加入列表
            self.w += cw                                # 对每次的位置做累加，最后取平均值
        self.w /= N                                     # 取平均值，增强稳定性
        return loss

    def predict(self, X):
        """ Lasso线性模型的预测函数 """
        return X.dot(self.w)
# end
     