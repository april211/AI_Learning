import numpy as np

X = np.array([2, 3, 1])

s = X.sum()                     # 求和
a = X.mean()                    # 求平均值
b = X.max()                     # 求最大值
i = X.argmax()                  # 求最大值对应的下标

print(s, a, b, i)
