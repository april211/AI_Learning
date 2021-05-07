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

plt.style.use('seaborn-darkgrid')
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
W = np.linspace(-1, 1, 500).reshape(500, 1)
W_poly = poly.fit_transform(W)

# Lambda=0.01
axs[0, 0].set_title("Lambda=0.01")
model = rr.RidgeRegression(Lambda=0.01)
model.fit(X_poly, y)
axs[0, 0].axis([-1, 1, -2, 2])
axs[0, 0].scatter(X, y)
u1 = model.predict(W_poly)
axs[0, 0].plot(W, u1)

# Lambda=0.1
axs[0, 1].set_title("Lambda=0.1")
model = rr.RidgeRegression(Lambda=0.1)
model.fit(X_poly, y)
axs[0, 1].axis([-1, 1, -2, 2])
axs[0, 1].scatter(X, y)
u2 = model.predict(W_poly)
axs[0, 1].plot(W, u2)

# Lambda=10
axs[1, 0].set_title("Lambda=10")
model = rr.RidgeRegression(Lambda=10)
model.fit(X_poly, y)
axs[1, 0].axis([-1, 1, -2, 2])
axs[1, 0].scatter(X, y)
u3 = model.predict(W_poly)
axs[1, 0].plot(W, u3)

# Lambda=100
axs[1, 1].set_title("Lambda=100")
model = rr.RidgeRegression(Lambda=100)
model.fit(X_poly, y)
axs[1, 1].axis([-1, 1, -2, 2])
axs[1, 1].scatter(X, y)
u4 = model.predict(W_poly)
axs[1, 1].plot(W, u4)

plt.show()



