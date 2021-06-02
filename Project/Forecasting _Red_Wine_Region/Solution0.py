import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import Softmax_Regression_SGD as srsgd
import Classification_Metrics as cm

def process_features(X):
    """ 数据标准化、加 1列 """
    m, n = X.shape
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X = np.c_[np.ones((m, 1)), X]
    return X


X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = process_features(X_train)
X_test = process_features(X_test)

# 训练时，需要由 m个 one-hot 标签向量构成的矩阵
encoder = OneHotEncoder()
Y_train = encoder.fit_transform(y_train.reshape(-1, 1)).reshape(-1, 3)

model = srsgd.SoftmaxRegressionSGD()
model.fit(X_train, Y_train, eta_0=50, eta_1=100, N=10000)

# 预测时，直出 0 ~ 2的数值预测标签
y_pred = model.predict(X_test)

# 计算准确率
accuracy = cm.accuracy_score(y_test, y_pred)
print("Accuracy: {}.".format(accuracy))
