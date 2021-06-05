import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import SVM_SMO as SVM
import matplotlib.pyplot as plt


def plot_figure(X, y, model):
    z = np.linspace(4, 8, 200)
    w = model.w
    b = model.b
    L = (-w[0] / w[1])* z - b / w[1]                                      # 二维绘图
    plt.scatter(X[:, 0][y[:, 0]==1], X[:, 1][y[:, 0]==1], c='r', s=5)     # 绘制正负样本点
    plt.scatter(X[:, 0][y[:, 0]==-1], X[:, 1][y[:, 0]==-1], c='b', s=5)
    plt.plot(z, L)                                                        # 绘制分离直线
    plt.show()
# end


iris = datasets.load_iris()
X = iris["data"][:, (0, 1)]
y = 2* (iris["target"]==0).astype(np.int64).reshape(-1, 1) - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

model = SVM.SVM_SMO()
model.fit(X_train, y_train, N=10)

print("Confidence coefficient: {}.".format(model.predict_confidence(X_test).reshape(1, -1)))       # 输出各测试点的预测置信度

plot_figure(X_train, y_train, model)
plot_figure(X_test, y_test, model)
