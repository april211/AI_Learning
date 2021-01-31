import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Linear_Regression_Class as lr
import matplotlib.pyplot as plt


def generate_samples(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


np.random.seed(100)
X, y = generate_samples(10)
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)
model = lr.LinearRegression()
model.fit(X_poly, y)

plt.axis([-1.5, 1.5, -3, 3])
plt.scatter(X, y)
W = np.linspace(-1, 1, 500).reshape(500, 1)
W_poly = poly.fit_transform(W)
u = model.predict(W_poly)
plt.plot(W, u)

plt.show()


"""
本代码并不能完成精确拟合
此处需要指出本代码的参考书：《机器学习算法导论》的一个错误，其在51页声称该代码可以精确拟合，且未作出任何其他说明
在本目录下的Solution2可以精确拟合（使用了Sklearn的线性模型），取自该参考书的官方代码库。其与原书代码并不相同。
希望该书再版时可以修改这个错误。
"""
