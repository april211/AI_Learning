import sys, os
import numpy as np
from sklearn.metrics import accuracy_score
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import SVM_SMO_SOFT as svm_soft
import matplotlib.pyplot as plt

def plot_figure(X, y, model):
    z = np.linspace(1, 8, 40)
    w = model.w
    b = model.b
    L = (-w[0] / w[1])* z - b / w[1]                                      # 二维绘图
    plt.scatter(X[:, 0][y[:, 0]==1], X[:, 1][y[:, 0]==1], c='r', s=5)     # 绘制正负样本点
    plt.scatter(X[:, 0][y[:, 0]==-1], X[:, 1][y[:, 0]==-1], c='b', s=5)
    plt.plot(z, L)                                                        # 绘制分离直线
    plt.show()
# end

iris = datasets.load_iris()
X = iris["data"][:, (2, 3)]
y = 2* (iris["target"]==2).astype(np.int64).reshape(-1, 1) - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

model = svm_soft.SoftSVM(C=5.0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy = {}".format(accuracy))

plot_figure(X_train, y_train, model)
plot_figure(X_test, y_test, model)
