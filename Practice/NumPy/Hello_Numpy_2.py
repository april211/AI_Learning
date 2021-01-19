import numpy as np

X = np.array([1, 2, 3])
Y = np.array([4, 5, 6])
Z = X + Y
U = X.dot(Y)                # 点积
a = 0.5
W = a * X                   # 数乘

print(X)
print(Y)
print(Z)
print(U)
print(W)
