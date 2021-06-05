import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import SVM_SMO as SVM
import matplotlib.pyplot as plt
import Classification_Metrics as cm

def plot_line(model):
    z = np.linspace(-2, 3, 10)
    w = model.w
    b = model.b
    L = (-w[0] / w[1])* z - b / w[1]                                      # 二维绘图
    plt.plot(z, L)                                                        # 绘制分离直线
# end

def one_versus_all(X, y, k):
    """ one_versus_all & SMO 实现 """
    m, n = X.shape
    testnum = np.int64(0.2* m)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testnum, random_state=0, stratify=y)
    H = np.empty(shape=(testnum, k))                                                    # 置信度矩阵
    for i in range(k):                                                                  # k元分类任务
        y_train_i = 2* (y_train == i).astype(np.int64).reshape(-1, 1) - 1               # 针对第 k类分类时的标签
        model = SVM.SVM_SMO()                                                           # 产生专门预测该类型的模型
        model.fit(X_train, y_train_i, N=10)
        y_pred_i = model.predict_confidence(X_test).reshape(-1, 1)      # 列向量
        H[:, i] = y_pred_i.reshape(testnum,)
        plot_line(model)
    y_pred = np.argmax(H, axis=1)                                       # 选取置信度最大的
    return y_pred, y_test


k = 3
X, y = make_blobs(n_samples=100, centers=k, n_features=2, cluster_std=0.2, random_state=0)      # 保证数据是线性可分的
y_pred, y_test = one_versus_all(X, y, k)

plt.scatter(X[:, 0][y==0], X[:, 1][y==0], c='r', s=5)
plt.scatter(X[:, 0][y==1], X[:, 1][y==1], c='b', s=5)
plt.scatter(X[:, 0][y==2], X[:, 1][y==2], c='y', s=5)
plt.scatter(X[:, 0][y==3], X[:, 1][y==3], c='purple', s=5)

plt.show()
