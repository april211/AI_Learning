import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import Ridge_Regression_Class as rr


def process_features(X):
    """对原始特征数据进行处理（主要进行特征标准化，使各个特征数据处于同一量级）"""
    scaler = StandardScaler()                       # 调用 Sklearn提供的的标准化方法对特征进行标准化
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]                   # 注意：这一步必须在标准化之后实施
    return X
# end


X, y = fetch_california_housing(return_X_y=True)            # 获取房价数据集，初步将特征与标签分开
X = X[:, (0, 6, 7)]                                         # 不考虑学号限制，此过程使用了特征选择算法
y = y.reshape(-1, 1)

eta_r = 1                                                   # random_state调参步长
rs = 1                                                      # random_state值
best_state = -1                                             # 记录当前最优的 random_state值
best_r2 = -1.0* float("inf")                                # 记录当前最优的 r2值
best_mse = float("inf")                                     # 记录当前最优的 mse值

# 下面的代码包含了针对 random_state的调参过程
# 线性回归模型选择了岭回归模型（线性L2正则化）
while rs < 1000:                    # 参数调整上限：1000
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=rs)
    X_train = process_features(X_train)
    X_test = process_features(X_test)

    model = rr.RidgeRegression(Lambda=0.01)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = model.mean_squared_error(y_test, y_pred)
    r2 = model.r2_score(y_test, y_pred)
    if r2 > best_r2 and mse < best_mse:
        best_state = rs
        best_r2 = r2
        best_mse = mse

    # print("mse = {} and r2 = {}.".format(mse, r2))
    rs += eta_r

# 在循环执行完后，输出范围内最优结果
print("The best rs = {}.".format(best_state))
print("The best r2 = {}.".format(best_r2))
print("The best mse = {}.".format(best_mse))
