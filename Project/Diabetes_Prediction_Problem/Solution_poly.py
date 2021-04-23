import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
import Linear_Regression_Class as lr



X, y = load_diabetes(return_X_y=True)
y = y.reshape(-1, 1)

poly = PolynomialFeatures(degree=1)            # 调用 Sklearn工具库中的类，将原始特征转化为指定次数的多项式特征
X = poly.fit_transform(X)                      # 使用内置方法，将原始特征二 (degree)次多项式化，以转化成线性模型问题

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


model = lr.LinearRegression()                  # 创建线性模型对象 (将 X_poly中的各分量看作线性模型中的不同特征)
model.fit(X_train, y_train)                    # 将问题转化成训练该·线性模型· """
y_pred = model.predict(X_test)
mse = model.mean_squared_error(y_test, y_pred)
r2 = model.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))



# https://blog.csdn.net/weixin_38278334/article/details/82971752
# https://blog.csdn.net/Eastmount/article/details/52929765
