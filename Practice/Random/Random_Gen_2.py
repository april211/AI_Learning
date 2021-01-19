import numpy as np
from numpy.random import Generator, PCG64           # 导入 PCG-64 BitGenerator

# We default to using a 128-bit integer using entropy gathered from the OS
sq1 = np.random.SeedSequence()
sq2 = np.random.SeedSequence()
print(sq1.entropy == sq2.entropy)           # 两个熵序列并不相等
print(sq2.generate_state(2, dtype=np.uint64))    # 第一个参数指定种子序列的长度，第二个指定种子类型

# rg = Generator(PCG64(sq1.generate_state(1, dtype=np.uint64)))
rg = Generator(PCG64(sq1.entropy))          # 直接将一个熵序列作为随机数种子

A = np.arange(12).reshape((3, 4))           # 产生一个 3 * 4 的自然数矩阵
print(A)

B = rg.choice(A, axis=1, size=5)            # 未改变矩阵 A
print(B)

rg.shuffle(A, axis=1)                       # 改变了矩阵 A
print(A)

print(rg.choice(5, 3, replace=False))       # 不重复地从 {0, 1, 2, 3, 4} 中取出 3个数
# This is equivalent to rg.permutation(np.arange(5))[:3]

print(rg.choice([-1.0, 2.0, 4.0], 2, replace=False))

""" If you need to generate a good seed “offline”, then SeedSequence().entropy or using secrets.randbits(128) from the standard library are both convenient ways. """

# https://numpy.org/doc/stable/reference/random/bit_generators/index.html
# https://numpy.org/doc/stable/reference/random/index.html#numpyrandom
