from __future__ import print_function

import torch


# Tensor (张量) 类似于NumPy的 ndarray，但还可以在 GPU上使用来加速计算

# 创建一个没有初始化的 5*3矩阵
x = torch.empty(5, 3)
print(x)

# 创建一个随机初始化矩阵
r = torch.rand(5, 3)
print(r)

# 构造一个填满 0且数据类型为 long的矩阵
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

# Constructs a tensor with data
x = torch.tensor([5.5, 3])
print(x)

# 根据已有的 tensor建立新的 tensor 
# 除非用户提供新的值，否则这些方法将重用输入张量的属性，例如 dtype等
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)    # 重载 dtype!
print(x)                                      # 结果size一致

# 获取张量的形状
# torch.Size本质上还是 tuple，所以支持 tuple的一切操作
print(x.size())


