import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

fig,axes = plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
	for j in range(2):
		axes[i,j].hist(randn(500),bins=50,color='k',alpha=0.5)
		
plt.subplots_adjust(wspace=0,hspace=0)  # 将比例收缩到0
plt.show()
