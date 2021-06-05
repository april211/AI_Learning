import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 样本数目、聚类中心数目、特征组维度、每个类别的方差（数组形式）、随机模式
X, y = make_blobs(n_samples=100, centers=3, n_features=2, cluster_std=0.2, random_state=10, center_box=(-10.0, 10.0))


""" print(X)
print(y) """

# X 有两列，每一行：(x1, x2)，作为数据点；y是标签值
plt.scatter(X[:, 0][y==0], X[:, 1][y==0], c='r', s=5)
plt.scatter(X[:, 0][y==1], X[:, 1][y==1], c='b', s=5)
plt.scatter(X[:, 0][y==2], X[:, 1][y==2], c='y', s=5)
""" plt.scatter(X[:, 0][y==3], X[:, 1][y==3], c='purple', s=5)
plt.scatter(X[:, 0][y==4], X[:, 1][y==4], c='orange', s=5) """

plt.show()


# https://www.jianshu.com/p/891f46e0125e
