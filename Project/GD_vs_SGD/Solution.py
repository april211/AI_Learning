import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_regression
import Linear_Regression_GD_Class as lrgd
import Linear_Regression_SGD_Class as lrsgd


X, y = make_regression(n_samples=100, n_features=2, noise=0.1, bias=0, random_state=0)
y = y.reshape(-1, 1)

model_1 = lrgd.LinearRegressionGD()
model_1.fit(X, y, eta=0.01, N=3000)
print(model_1.w)

model_2 = lrsgd.LinearRegressionSGD()
model_2.fit(X, y, eta_0=10, eta_1=50, N=3000)
print(model_2.w)
