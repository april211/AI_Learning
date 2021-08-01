import torch

# 6* 13* 13
x = torch.linspace(0, 13 - 1, 13).repeat(13, 1).repeat(
            2 * 3, 1, 1)

print(x)
print(x.shape)

y = x.view([2, 3, 13, 13])

print(y.shape)
print(y)
