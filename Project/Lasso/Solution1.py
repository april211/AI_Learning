import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Lasso_SGD_SubGD_Class as lss
import matplotlib.pyplot as plt
import Classification_Metrics as cm

""" 结合 随机梯度下降 & 次梯度的Lasso回归 """

def generate_samples(m):
    X = 4* (np.random.rand(m, 1) - 0.5)
    y = X**2 + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


np.random.seed(100)
X, y = generate_samples(40)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = lss.Lasso(Lambda=0.01)                  # 0.001 -> 0.01 -> 0.1 -> 0.5
loss = model.fit(X_poly, y, eta_0=10, eta_1=50, N=3000)


plt.style.use('seaborn-darkgrid')
fig, axs = plt.subplots(1, 2, figsize=(9, 4))
plt.subplots_adjust(wspace=0.4)

# 做出拟合曲线图
axs[0].set_title("SGD & SubGD Fitted Curve")
axs[0].scatter(X, y, s=5)
LX = np.linspace(-2, 2, 400).reshape(400, 1)
LX_poly = poly.fit_transform(LX)
y_pred = model.predict(LX_poly)
axs[0].plot(LX, y_pred)

# 绘制收敛过程图
axs[1].set_title("Convergence Procedure")
axs[1].set_xlabel("Iterations")
axs[1].set_ylabel("mean_squared_error")
tepoch = np.arange(start=0, stop=3000).reshape(3000, 1)
axs[1].plot(tepoch[:200], loss[:200])           # 节选了 [20:200]这部分进行绘制，更容易看出前期的变化

plt.show()


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
