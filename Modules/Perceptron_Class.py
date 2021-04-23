import numpy as np

class Perceptron:
    """感知器类型"""
    def __init__(self) -> None:
        self.maxn = 2000                         # 设置最大迭代次数，防止陷入死循环

    def fit(self, X, y):
        """训练模型并存储训练得到的参数"""
        m, n = X.shape                          # m表示训练数据的数目，n代表特征数目
        w = np.zeros((n, 1))                    # 初始化参数 w的列向量为一个零向量 (n * 1)
        b = 0                                   # 初始化参数 b为零
        done = False
        cnt = 0
        while (not done) and (cnt < self.maxn):
            done = True
            cnt += 1
            for i in range(m):
                x = X[i].reshape(1, -1)            # 保证该训练数据是一个 (1 * n) 维的行向量，以供后面的内积运算
                if (y[i]* (np.sign(x.dot(w) + b)) <= 0):    # 等于 0时也进行调整
                    w += y[i]* x.T                 # x.T : (n * 1)
                    b += y[i]
                    done = False
        self.w = w
        self.b = b

    def predict(self, X):                          # X为测试数据，是一个行向量
        """用训练好的模型对给定数据进行预测"""
        return np.sign(X.dot(self.w) + self.b)
# end
    