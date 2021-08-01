from __future__ import print_function

import torch


# 加法：形式 1
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x + y)

# 加法：形式 2
print(torch.add(x, y))

# 加法：给定一个输出张量作为参数
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

# 加法：原位/原地操作 (in-place)
# 任何一个 in-place改变张量的操作后面都固定一个_。例如x.copy_(y)、x.t_()将更改x
# adds x to y
y.add_(x)
print(y)

# 也可以使用像标准的 NumPy一样的各种索引操作
print(y[:, 1])

# 改变形状：如果想改变形状，可以使用 torch.view
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())
print(x)
print(y)
print(z)

# 如果是仅包含一个元素的 tensor，可以使用.item()来得到对应的 python数值
x = torch.randn(1)
print(x)
print(x.item())
