import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator, PCG64           # 导入 PCG-64 BitGenerator


sq1 = np.random.SeedSequence()
np.random.seed(sq1.generate_state(1, dtype=np.uint32)[0])       # 指定 32位随机数种子

X = np.random.rand(100, 2)

plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.show()
