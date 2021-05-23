import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import Classification_Metrics as cm


def process_features(X):
    """对原始特征数据进行处理（主要进行特征标准化，使各个特征数据处于同一量级）"""
    scaler = StandardScaler()                       # 调用 Sklearn提供的的标准化方法对特征进行标准化
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]                   # 注意：这一步必须在标准化之后实施
    return X
# end

def nablaF(X, y, w):
    return np.matrix(2* X.T.dot(X).dot(w) - 2* X.T.dot(y))
# end

def nabla2F(X, y, w):
    return np.matrix(2* X.T.dot(X))
# end

housing = fetch_california_housing()
X = housing.data
y = housing.target.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = process_features(X_train)
X_test = process_features(X_test)

w = np.zeros(9).reshape(9, -1)          # 8个特征，与上面加 1列一致，有 8 + 1 == 9 个分量
epsilon = 0.1
max_iter = 10000

while (np.linalg.norm(nablaF(X_train, y_train, w), ord=2) > epsilon) and (max_iter > 0):
    w -= (nabla2F(X_train, y_train, w)).I.dot(nablaF(X_train, y_train, w))
    max_iter -= 1

y_pred = X_test.dot(w)
mse = cm.mean_squared_error(y_test, y_pred)
r2 = cm.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))
