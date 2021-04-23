import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
import Ridge_Regression_Class as rr



X, y = load_diabetes(return_X_y=True)
y = y.reshape(-1, 1)

poly = PolynomialFeatures(degree=5)            # 调用 Sklearn工具库中的类，将原始特征转化为指定次数的多项式特征
X = poly.fit_transform(X)                      # 使用内置方法，将原始特征二 (degree)次多项式化，以转化成线性模型问题

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = rr.RidgeRegression(Lambda=0.0051)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = model.mean_squared_error(y_test, y_pred)
r2 = model.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))
