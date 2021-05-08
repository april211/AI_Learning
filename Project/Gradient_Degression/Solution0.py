import sys, os
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.getcwd() + r'\Modules')


def func(w):
    return w**2 - w + 1
# end

def func_d(w):
    return 2* w - 1
# end

x_start = 0                     # 起始点
eta = 0.6                       # 步长
iter_cnt = 5                    # 迭代次数

fig, ax = plt.subplots(1, 1, figsize=(9, 4))
X = np.linspace(-0.1, 1.1, 500)
FX = func(X)
ax.plot(X, FX)
ax.scatter(x_start, func(x_start), c='r', s=8)
ITX = np.array([])

for i in range(iter_cnt):
    x_start = x_start - eta* func_d(x_start)
    ITX = np.append(ITX, x_start)

ax.scatter(ITX, func(ITX), c='g', s=6)

print(ITX, func(ITX))

plt.show()
