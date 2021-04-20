import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from Perceptron_Class import Perceptron

# 样本数目、聚类中心数目、特征组维度、每个类别的方差（数组形式）、随机模式
X, y = make_blobs(n_samples=100, centers=2, n_features=2, cluster_std=0.6, random_state=0)

for i in range(0, 100):
    if y[i] == 0:
        y[i] = -1

# 分离训练数据和测试数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = Perceptron()
model.fit(X_train, y_train)
model.predict(X_test)

plt.style.use('seaborn-darkgrid')                       # 在两个坐标系中分别画出训练数据点与测试数据点
fig, axs = plt.subplots(1, 2, figsize=(9, 4))           # a figure with a 1x2 grid of Axes
axs[0].scatter(X_train[:, 0], X_train[:, 1], c=list(y_train), cmap=plt.cm.seismic, edgecolors='none', s=6)
axs[1].scatter(X_test[:, 0], X_test[:, 1], c=list(y_test), cmap=plt.cm.seismic, edgecolors='none', s=6)

LX1 = np.linspace(-1.0, 4.0, 200)                     # 在两个坐标系中画出模型直线
LX2 = ((-1.0)* (model.w[0])* LX1 - model.b) / (model.w[1])
axs[0].plot(LX1, LX2, linewidth=1)
axs[1].plot(LX1, LX2, linewidth=1)

# X 有两列，每一行：(x1, x2)，作为数据点；y是标签值
# plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs", ms=3)          # 以蓝色实心方块显示
# plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo", ms=3)          # 以黄色实心圆表示，ms表示点的大小

plt.show()


# https://www.jianshu.com/p/891f46e0125e
