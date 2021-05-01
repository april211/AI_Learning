from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt




fig, ax = plt.subplots(1, 1)
dfn, dfd = 4, 4
mean, var, skew, kurt = f.stats(dfn, dfd, moments='mvsk')

x = np.linspace(f.ppf(0.001, dfn, dfd), f.ppf(0.599, dfn, dfd), 1000)          # 反函数

ax.plot(x, f.pdf(x, dfn, dfd), 'r-', lw=2, alpha=0.7, label='f pdf')           # alpha: 色深

plt.show()
