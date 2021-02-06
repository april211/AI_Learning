import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import Linear_Regression_SGD_Class as lrsgd


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

model = lrsgd.LinearRegressionSGD()
model.fit(X_train, y_train, eta_0=10, eta_1=50, N=3000)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("mse = {}, r2 = {}.".format(mse, r2))
