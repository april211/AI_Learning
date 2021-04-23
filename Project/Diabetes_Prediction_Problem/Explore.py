from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt


""" 
(442, 10)
(442,)
"""

X, y = load_diabetes(return_X_y=True)
print(X)
print(y)
print(X.shape)
print(y.shape)

