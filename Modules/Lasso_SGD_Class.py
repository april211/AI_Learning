import numpy as np


class Lasso:
    """ Lasso回归问题的次梯度下降解决方案 """
    def __init__(self, Lambda=1):
        """ 初始化正则化强度参数 """
        self.Lambda = Lambda

    def fit(self, X, y, eta=0.1, N=1000):
        """ Lasso线性模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1)).reshape(-1, 1)                   # 当前位置
        self.w = np.zeros((n, 1)).reshape(-1, 1)               # *** 这里请看下面的解释 ***
        for t in range(N):
            e = X.dot(cw) - y
            v = (2* X.T.dot(e) / m) + (self.Lambda* np.sign(cw))     # 正则化部分使用了次梯度的概念（选择了一个）
            cw -= eta* v                                # 若按照原书，这里这样写会出现错误
            self.w += cw                                # 对每次的位置做累加，最后取平均值
        self.w /= N                                     # 取平均值，增强稳定性

    def predict(self, X):
        """ Lasso线性模型的预测函数 """
        return X.dot(self.w)
# end


"""
个人看法：针对列表这类对象，能深拷贝就深拷贝，否则稍有不慎，就会出现一些莫名其妙的错误。

完全按照原书（代码库）的代码：

self.w = w
...
w = w - eta* v

去写，也能正常运行并得出正确结果。
但是现在的问题是：如果是把上面第二行代码改成：w -= eta* v 呢？是不是觉得：这不是一样吗？？
结果是：不一样。
实际运行时，会出现 overflow 等警告，并且不能得到正确的拟合曲线（在我这里的图像上直接没有曲线）
若将上面的第一行代码改为深拷贝的形式：

self.w = cw.copy()

后，后面不管怎么写（我那种自减写法或者上面第二行代码的写法）都行，实际运行也完全没问题。
就算不用深拷贝，这样写：

sumw = np.zeros((n, 1)).reshape(-1, 1)

最后面那部分算平均的部分再改一改，也完全没问题（感觉这相当于是“进行了深拷贝”，因为是一块新的内存）。
个人感觉我自己的写法更加符合 “思维惯性”。
也有可能是其他原因导致的。但是截止到现在，我认为问题就是浅拷贝导致的。
现在就先这样吧。

"""
     