import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import Softmax_Regression_GD as srgd
import Classification_Metrics as cm


def process_features(X):
    scaler = MinMaxScaler(feature_range=(0, 1))
    X = scaler.fit_transform(1.0* X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X
# end


iris = datasets.load_iris()
X = iris["data"]
Y = iris["target"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
X_train = process_features(X_train)
X_test = process_features(X_test)

encoder = OneHotEncoder()
Y_train = encoder.fit_transform(Y_train.reshape(-1, 1)).toarray()  # 将自然数数标签转化成三维的 0-1向量标签的形式

model = srgd.SoftmaxRegressionGD()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)                  # 此处预测类别表示为自然数
accuracy = cm.accuracy_score(Y_test, Y_pred)    # Y_test为自然数标签

print("Accuracy = {}.".format(accuracy))


# https://www.cnblogs.com/zhoukui/p/9159909.html
