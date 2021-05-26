import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import Logistic_Regression_L2_GD as lrl2


def process_features(X):
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X
# end


iris = datasets.load_iris()
X = iris["data"]
y = (iris["target"]==2).astype(np.int).reshape(-1, 1)       # 列向量
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train = process_features(X_train)
X_test = process_features(X_test)

model = lrl2.LogisticRegressionL2GD(Lambda=0.01)
model.fit(X_train, y_train, eta=0.1, N=10000)
proba = model.predict_proba(X_test)
entropy = model.cross_entropy(y_test, proba)

print("Cross entropy = {}.".format(entropy))
