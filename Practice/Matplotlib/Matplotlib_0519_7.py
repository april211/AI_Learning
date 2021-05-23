import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10)
y = np.random.randint(0,30,10)
plt.bar(x, y)                       # 绘制条形图（柱状图）

plt.show()
