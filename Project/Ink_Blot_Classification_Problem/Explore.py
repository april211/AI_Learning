import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from Perceptron_Class import Perceptron

# 样本数目、聚类中心数目、特征组维度、每个类别的方差（数组形式）、随机模式
X, y = make_blobs(n_samples=100, centers=2, n_features=2, cluster_std=0.6, random_state=0)

for i in range(0, 100):
    if y[i] == 0:
        y[i] = -1

print(X)
print(y)

# X 有两列，每一行：(x1, x2)，作为数据点；y是标签值
# plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs", ms=3)          # 以蓝色实心方块显示
# plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo", ms=3)          # 以黄色实心圆表示，ms表示点的大小

# plt.show()


# https://www.jianshu.com/p/891f46e0125e
