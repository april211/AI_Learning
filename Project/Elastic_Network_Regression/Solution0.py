import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Elastic_Network_Regression as enr
import matplotlib.pyplot as plt


def generate_samples(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


np.random.seed(100)
X, y = generate_samples(20)
poly = PolynomialFeatures(degree=6)
X_poly = poly.fit_transform(X)

model1 = enr.ElasticNetwork(Lambda=0.1, r=0.2)          # 调用弹性网回归模型
model1.fit(X_poly, y, N=2000)

plt.style.use('seaborn-darkgrid')
fig, axs = plt.subplots(1, 2, figsize=(9, 4))
plt.subplots_adjust(wspace=0.2)

axs[0].set_title("Lambda=0.1, r=0.2")
axs[0].scatter(X, y, s=5, c='c')
LX = np.linspace(-1, 1, 400).reshape(400, 1)
LX_poly = poly.fit_transform(LX)
y_pred = model1.predict(LX_poly)
axs[0].plot(LX, y_pred)

model2 = enr.ElasticNetwork(Lambda=0.1, r=0.7)          # 调用弹性网回归模型
model2.fit(X_poly, y, N=2000)

axs[1].set_title("Lambda=0.1, r=0.7")
axs[1].scatter(X, y, s=5, c='c')
y_pred = model2.predict(LX_poly)
axs[1].plot(LX, y_pred)

plt.show()
