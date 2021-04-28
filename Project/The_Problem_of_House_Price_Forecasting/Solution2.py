import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import Stagewise_Regression_Class as sr
import Classification_Metrics as cm


# 特征标准化、添 “1” 列
def process_features(X):
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X

X, y = fetch_california_housing(return_X_y=True)            # 获取房价数据集，初步将特征与标签分开
y = y.reshape(-1, 1)
# print(X.shape)

# 使用保留法直接切分源数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 处理测试集、训练集的特征矩阵
X_train = process_features(X_train)
X_test = process_features(X_test)

model = sr.StagewiseRegression()
model.feature_selection(X_train, y_train, 4000, 0.02)
y_pred = model.predict(X_test)

mse = cm.mean_squared_error(y_test, y_pred)
r2 = cm.r2_score(y_test, y_pred)

wc = np.abs(np.copy(model.w))[1:]

print(wc)

for i in range(3):
    idx = np.argmax(wc)
    print("Attribute: {}".format(idx))
    wc[idx] = -1.0* float("inf")

print("mse = {} and r2 = {}.".format(mse, r2))
