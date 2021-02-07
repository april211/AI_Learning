import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Lasso_SGD_Class as lc
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
model = lc.Lasso(Lambda=0.1)                  # 0.001 -> 0.01 -> 0.1 -> 0.5
model.fit(X_poly, y, eta=0.01, N=50000)

plt.axis([-1, 1, -2, 2])
plt.scatter(X, y)
W = np.linspace(-1, 1, 100).reshape(100, 1)
W_poly = poly.fit_transform(W)
u = model.predict(W_poly)
plt.plot(W, u)

plt.show()
