import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import Linear_Regression_GD_Class as lrgd
import matplotlib.pyplot as plt


def process_features(X):
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X
# end


housing = fetch_california_housing()
X = housing.data
y = housing.target.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train = process_features(X_train)
X_test = process_features(X_test)

eta = 0.01
N = 100
eta_list = np.empty(shape=(1, 0))
r2_list = np.empty(shape=(1, 0))
N_list = np.empty(shape=(1, 0))

# 固定 N = 6000，测试 eta
for i in range(30):
    model1 = lrgd.LinearRegressionGD()
    model1.fit(X_train, y_train, eta, 6000)
    y_pred = model1.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    eta_list = np.append(eta_list, eta)
    r2_list = np.append(r2_list, r2)
    # print("mse = {}, r2 = {}.".format(mse, r2))
    print(eta)
    eta += 0.005

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].set_title('r2 ~ eta', size=20)
axs[0].plot(eta_list, r2_list, c='b', linewidth=2)

r2_list = np.empty(shape=(1, 0))

# 固定 eta = 0.14，测试 N
for i in range(20):
    model2 = lrgd.LinearRegressionGD()
    model2.fit(X_train, y_train, 0.14, N)
    y_pred = model2.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    N_list = np.append(N_list, N)
    r2_list = np.append(r2_list, r2)
    # print("mse = {}, r2 = {}.".format(mse, r2))
    print(N)
    N += 400

axs[1].set_title('r2 ~ N', size=20)
axs[1].plot(N_list, r2_list, c='g', linewidth=2)

plt.show()
