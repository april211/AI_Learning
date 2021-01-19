import numpy as np

m = 3

X = np.random.rand(m, m)
Y = np.linalg.inv(X)            # 求方阵的逆矩阵

print(X)
print(Y)
