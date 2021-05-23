import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

fig,axes = plt.subplots(2,3)
print(axes)
axes[0,1].hist(randn(100),bins=20,color='green',alpha=0.3)

plt.show()
