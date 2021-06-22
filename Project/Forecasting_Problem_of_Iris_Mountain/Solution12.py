import sys, os
import numpy as np
from sklearn.metrics import accuracy_score
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import SVM_SOFT_SGD as svm_soft_sgd
import matplotlib.pyplot as plt


def rbf_kernel(x1, x2):
    """径向基核函数（高斯核函数） x1, x2: vector"""
    sigma = 1.0
    return np.exp((-1.0 / (2.0* (sigma**2)))* np.linalg.norm(x1-x2, ord=2)** 2)
# end


iris = datasets.load_iris()
X = iris["data"][:, (2, 3)]
y = 2* (iris["target"]==2).astype(np.int64).reshape(-1, 1) - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

model = svm_soft_sgd.SoftSVM(C=9.0)
model.fit(X_train, y_train, eta=0.1, N=20000)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("accuracy = {}".format(accuracy))

xs = np.linspace(1, 7, 100)
ys = np.linspace(0, 3, 100)
x, y = np.meshgrid(xs, ys)          # x, y's shape: (100, 100)

W = np.c_[np.ravel(x).reshape(-1, 1), np.ravel(y).reshape(-1, 1)]
u = model.predict(W).reshape(x.shape)

plt.scatter(X_train[:, 0][y_train[:, 0]==1], X_train[:, 1][y_train[:, 0]==1], c='r', s=5)
plt.scatter(X_train[:, 0][y_train[:, 0]==-1], X_train[:, 1][y_train[:, 0]==-1], c='b', s=5)
plt.contourf(x, y, u, alpha=0.4)

plt.show()
