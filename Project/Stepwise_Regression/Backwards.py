import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import Stepwise_Regression_BW_Class as srbw


X = np.array(
      [[0.06, 0.34, 0.03]
      ,[0.44, 0.76, 0.28]
      ,[0.86, 0.44, 0.20]
      ,[0.26, 0.09, 0.25]])                     # X ~ N(x1 + 2* x2, 1)

y = np.array([[0.42]
             ,[1.32]
             ,[0.84]
             ,[0.61]])

model = srbw.StepwiseRegressionBW()
model.backward_selection(X, y)
y_pred = model.predict(X)

print(model.A)
print(model.w, model.w.shape)
print(y_pred)
