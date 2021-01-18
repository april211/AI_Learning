import numpy as np

X = np.array([[1, 2, 3],
              [4, 5, 6]])

# 在保持矩阵元素个数不变的前提下，重塑矩阵
Y = X.reshape(1, 6)
Z = X.reshape(3, 2)
W = X.reshape(6, 1)

print(X)
print(Y)
print(Z)
print(W)
