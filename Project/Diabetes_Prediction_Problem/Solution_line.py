import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
import Linear_Regression_Class as lr


def process_features(X):
    """对原始特征数据进行处理（主要进行特征标准化，使各个特征数据处于同一量级）"""
    scaler = StandardScaler()                       # 调用 Sklearn提供的的标准化方法对特征进行标准化
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]                   # 注意：这一步必须在标准化之后实施
    return X
# end


X, y = load_diabetes(return_X_y=True)
y = y.reshape(-1, 1)
X = process_features(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


model = lr.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = model.mean_squared_error(y_test, y_pred)
r2 = model.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))
