import numpy as np
from numpy.random import Generator, PCG64



sq1 = np.random.SeedSequence()
rg = Generator(PCG64(sq1.entropy))          # 直接将一个熵序列作为随机数种子

X = rg.uniform(0, 1, (10, 3)).reshape(10, 3)
y = rg.normal(X[:, 1] + 2* X[:, 2], 0.1).reshape(-1, 1)

print(X)
print(y)




# https://numpy.org/doc/stable/reference/random/generator.html?highlight=generator#numpy.random.Generator
