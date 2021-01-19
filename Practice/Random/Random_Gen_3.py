import numpy as np
from numpy.random import Generator, PCG64

sq1 = np.random.SeedSequence()

# 尝试产生指定范围内的随机浮点数
# 法一
np.random.seed(sq1.generate_state(1, dtype=np.uint32)[0])       # 指定 32位随机数种子
a, b = 3.0, 7.0
rn1 = (b - a) * np.random.random_sample() + a
X = 5.0 * np.random.random_sample((3, 2)) - 5.0             # Three-by-two array of random numbers from [-5, 0)
print(rn1)
print(X)

# 法二（这样做更符合新标准）
rg = Generator(PCG64(sq1.entropy))          # 直接将一个熵序列作为随机数种子
rn2 = (b - a) * rg.random() + a
Y = 5.0 * rg.random((3, 2)) - 5.0             # Three-by-two array of random numbers from [-5, 0)
print(rn2)
print(Y)

"""
Results are from the “continuous uniform” distribution over the stated interval. To sample Unif[a, b), b > a multiply the output of random_sample by (b-a) and add a:
                                    (b - a) * random_sample() + a
"""

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random
# https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState
# https://numpy.org/doc/stable/reference/random/generator.html?highlight=numpy%20random%20generator#numpy.random.Generator
