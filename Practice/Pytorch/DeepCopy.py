import torch
import torch.nn as nn


x = torch.tensor([[1, 2, 3],
                  [2, 3, 4]])

y = x
x[1, 2] = 100

print(x)
print(y)

z = x.clone()           # 不共享数据内存，不脱离计算图
x[0, 1] = 77

print(x)
print(z)

layer1 = nn.Conv2d(3, 2, kernel_size=1, stride=1, padding=0, bias=False)
layer2 = nn.Conv2d(2, 1, kernel_size=1, stride=1, padding=0, bias=False)

p = torch.tensor([[[[1, 2], 
                    [3, 4]],
                   [[1, 2], 
                    [3, 4]],
                   [[1, 2], 
                    [3, 4]]]]).float()
print(p.shape)
p = layer1(p)
o = p
p = layer2(p)                   # 隐式深拷贝
print(o)
print(p)
