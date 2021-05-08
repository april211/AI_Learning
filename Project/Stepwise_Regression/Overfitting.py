import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Stepwise_Regression_Class as sr
import matplotlib.pyplot as plt


def generate_sample(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


np.random.seed(100)
X, y = generate_sample(10)
poly = PolynomialFeatures(degree=10)            # 多项式特征
X_poly = poly.fit_transform(X)

model = sr.StepwiseRegression()
model.forward_selection(X_poly, y)              # 执行特征选择操作
print(model.A)
print(model.w)

plt.axis([-1, 1, -2, 2])
plt.scatter(X, y)
W = np.linspace(-1, 1, 500).reshape(500, 1)
W_poly = poly.fit_transform(W)
u = model.predict(W_poly)                       # 使用训练得到的线性模型进行预测
plt.plot(W, u)

plt.show()
