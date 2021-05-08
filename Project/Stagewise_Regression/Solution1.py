import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import Stagewise_Regression_Class as sr


def generate_sample(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


# 生成多项式特征
np.random.seed(100)
X, y = generate_sample(10)
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)

model = sr.StagewiseRegression()
model.feature_selection(X_poly, y, 1000, 0.001)

fig, ax = plt.subplots(1, 1, figsize=(5, 4))
ax.axis([-1, 1, -2, 2])
ax.scatter(X, y)                        # 打印原特征和标签点

LX = np.linspace(-1, 1, 500).reshape(500, 1)            # 预测 linspace生成的各点（注意这里需要 reshape）
LX_poly = poly.fit_transform(LX)
y_pred = model.predict(LX_poly)
ax.plot(LX, y_pred)

plt.show()
