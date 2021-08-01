import torch
import numpy as np


# 下面的这个操作不是数乘，是 repeat !
print(torch.tensor([2, 3] * 4))

# 原因起源于 python list
x = [2, 3]* 4
print(x)

# 这样是数乘
y = np.array([2, 3])
print(y* 4)

# 这样也是数乘
z = torch.tensor([2, 3])* 4
print(z)
