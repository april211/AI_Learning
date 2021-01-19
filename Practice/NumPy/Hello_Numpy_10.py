import numpy as np

def func(a):
    a += 1
# end

X = np.array([[1, 2, 3],
              [4, 5, 6]])

func(X)                         # 定义在实数域上的矩阵都可以拓展到矩阵上
print(X)
