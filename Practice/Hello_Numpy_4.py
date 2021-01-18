import numpy as np

m, n = 2, 3
shape = (m, n)                 # 矩阵尺寸：2 * 3（代数意义上）

X = np.zeros(shape)            # 生成指定大小的全零矩阵
Y = np.ones(shape)             # 生成指定大小的全一矩阵
Z = np.random.rand(m, n)       # 生成指定大小的随机数矩阵

A = [[1, 2, 3],
     [4, 5, 6]]
W = np.array(A)                 # 将普通的二维数组转换成 NumPy数组

print(X)
print(Y)
print(Z)
print(A)
print(W)

print(W.shape)
