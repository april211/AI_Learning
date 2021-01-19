import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator, PCG64           # 导入 PCG-64 BitGenerator


sq1 = np.random.SeedSequence()
rg = Generator(PCG64(sq1.entropy))          # 直接将一个熵序列作为随机数种子

X = rg.integers(low=0, high=29, size=(81, 2), dtype=np.int64, endpoint=False)
print(X)

plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.show()
