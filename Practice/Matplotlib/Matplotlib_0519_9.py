import matplotlib.pyplot as plt
import numpy as np

mean, sigma = 0, 1
x = mean + sigma * np.random.randn(10000)
plt.hist(x,50)              # 绘制直方图

plt.show()
