import numpy as np

X = np.array([[1, -1.0],
              [1, 0.0],
              [1, 1.0]])

y = np.array([[-1.2],
              [1.0],
              [2.8]])

print(X.T.dot(X))
print(np.linalg.inv(X.T.dot(X)))

w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
print(w)
