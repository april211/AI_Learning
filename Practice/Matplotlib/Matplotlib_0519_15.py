import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

fig = plt.figure()   # 创建对象
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.plot(randn(50).cumsum(),'k--')

ax1.hist(randn(100),bins=20,color='k',alpha=0.3)  # 20个直方图,alpha透明度
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))  # 绘制散点图
plt.show()
