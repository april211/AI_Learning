import numpy as np

X = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

i, j = 1, 3
p, q = 1, 3
Y = X[i:j, p:q]             # 矩阵切片

print(X)
print(Y)
