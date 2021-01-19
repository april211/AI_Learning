import numpy as np

m, n, k = 3, 2, 4

X = np.random.rand(m, n)
Y = np.random.rand(n, k)

Z = X.dot(Y)                # 利用推广内积实现矩阵相乘

print(X)
print(Y)
print(Z)
