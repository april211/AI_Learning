import numpy as np
import matplotlib.pyplot as plt

""" 这个实例简单地展示了牛顿迭代法的收敛过程 """

def F(w):
    """ f(w) = w^2 """
    return w**2
# end

def dF(w):
    """ f'(w) = 2w """
    return 2* w
# end


x, y = [], []
epsilon = 1e-4                          # 设置精度
w = -1.5                                # 起始位置

while abs(F(w)) > epsilon:
    x.append(w)
    y.append(F(w))
    w -= F(w) / dF(w)                  # w = w - F(w) / F'(w)

print(w)

# 数据可视化部分
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y, c=list(x), cmap=plt.cm.seismic, edgecolors='none', s=10)

LX = np.linspace(-2.0, 2.0, 100)
LY = F(LX)
ax.plot(LX, LY, linewidth=1)

plt.show()
