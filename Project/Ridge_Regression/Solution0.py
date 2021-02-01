import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import Ridge_Regression_Class as rr


def generate_samples(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


np.random.seed(100)
X, y = generate_samples(10)
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)
model = rr.RidgeRegression(Lambda=0.01)
model.fit(X_poly, y)

plt.axis([-1, 1, -2, 2])
plt.scatter(X, y)
W = np.linspace(-1, 1, 500).reshape(500, 1)
W_poly = poly.fit_transform(W)
u = model.predict(W_poly)
plt.plot(W, u)

plt.show()

"""
注意：
参考书上的本例代码所使用的岭回归类（详见/Modules）与官方代码库中的岭回归类写法不同，
这里选择了官方代码库上的版本。
若不使用官方代码库的版本，则不能实现原书32页的目标拟合图像。
"""
