import numpy as np
from numpy.random import Generator, PCG64           # 导入 PCG-64 BitGenerator

sq1 = np.random.SeedSequence()
rg = Generator(PCG64(sq1.entropy))          # 直接将一个熵序列作为随机数种子

# 指定多个上界，分别产生随机数，并将结果合并入一个列表中
print(rg.integers(1, [3, 5, 10]))           # Generate a 1 x 3 array with 3 different upper bounds
print(rg.integers([1, 5, 7], 10))           # Generate a 1 by 3 array with 3 different lower bounds


# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers
