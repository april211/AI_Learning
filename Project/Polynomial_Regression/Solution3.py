import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import Linear_Regression_Class as lr
import matplotlib.pyplot as plt

X = [[0],
     [1],
     [2]]               # 特征组

y = [[1],               # 标签
     [1],
     [3]]

poly = PolynomialFeatures(degree=2)     # 调用 Sklearn工具库中的类，将原始特征转化为指定次数的多项式特征
X_poly = poly.fit_transform(X)          # 使用内置方法，将原始特征二 (degree)次多项式化，以转化成线性模型问题
model = lr.LinearRegression()           # 创建线性模型对象 (将 X_poly中的各分量看作线性模型中的不同特征)
model.fit(X_poly, y)                    # 将问题转化成训练该·线性模型·

# 绘制训练点集、与之拟合的多项式函数图线
plt.scatter(X, y)
W = np.linspace(-4, 5, 300).reshape(300, 1)
W_poly = poly.fit_transform(W)                      # 特征多项式化，以供训练得到的·线性模型·使用
u = model.predict(W_poly)                           # 由线性模型预测获得标签值
plt.plot(W, u)

plt.show()

# print(X_poly)
