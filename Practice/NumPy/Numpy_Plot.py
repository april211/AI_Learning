import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 100)         # 在 -5 到 5 之间生成 100 个等间隔数
Y = np.sin(X)

plt.figure(0)
plt.plot(X, Y)
plt.show()
