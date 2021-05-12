import numpy as np
import matplotlib.pyplot as plt


def func(w):
    """ 原函数 """
    return (w - 1)**2
# end

def func_1d(w):
    """ 原函数的一阶导函数 """
    return 2* (w - 1)
# end

def func_2d(w):
    """ 原函数的二阶导函数 """
    return 2
# end

x, y = np.array([]), np.array([])
w_iter = 0                      # 起始位置
epsilon = 1e-7                  # 计算精度
iter_cnt = 0                    # 迭代次数计数器

# 牛顿迭代部分
while abs(func(w_iter)) > epsilon:
    iter_cnt += 1
    x = np.append(x, w_iter)
    y = np.append(y, func(w_iter))
    w_iter -= func_1d(w_iter) / func_2d(w_iter)

x = np.append(x, w_iter)                                           # 将结束位置录入迭代列表
y = np.append(y, func(w_iter))
print("Number of iteration(s): {}.".format(iter_cnt))
print("Solution: {}, value: {}.".format(w_iter, func(w_iter)))

# 迭代过程可视化
fig, ax = plt.subplots(1, 1, figsize=(5, 4))
LX = np.linspace(-3, 5, 800)
FLX = func(LX)
ax.plot(LX, FLX)
ax.scatter(x, y, c='g', s=8)

plt.show()
