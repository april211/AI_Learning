import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import matplotlib.pyplot as plt

def generate_samples(m):
    X = 2* (np.random.rand(m, 1) - 0.5) 
    y = X + np.random.normal(0, 0.3, (m,1))
    return X, y
# end


np.random.seed(100)
X, y = generate_samples(10)
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)
model = linear_model.LinearRegression()
model.fit(X_poly, y)

plt.axis([-1, 1, -2, 2])
plt.scatter(X, y)
W = np.linspace(-1, 1, 500).reshape(500, 1)
W_poly = poly.fit_transform(W)
u = model.predict(W_poly)
plt.plot(W, u)

plt.show()




# https://github.com/wanglei18/machine_learning/blob/master/Codes/linear_regression/degree_10_poly.py
