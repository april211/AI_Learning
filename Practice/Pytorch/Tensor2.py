from __future__ import print_function

import torch
import numpy as np

# tensor向 numpy ndarray的转换
# 返回 tensor底层的 numpy数据结构的引用
x = torch.ones(4, 4)
y = x.numpy()

print(x)
print(y)

# 修改此 numpy数据结构，对应的 tensor也发生改变
y[:, 2] = 0
print(x)


# numpy ndarray向 tensor的转换
a = np.ones((2, 2))
b = torch.from_numpy(a)
print(a)
print(b)

# 修改此 numpy数据结构，对应的 tensor也发生改变
a[:, 1] = 3
print(b)

# CPU上的所有张量(CharTensor除外)都支持与Numpy的相互转换。
print(torch.cuda.is_available())
