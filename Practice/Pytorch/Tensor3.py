from __future__ import print_function

import torch
import numpy as np


x = torch.ones(4, 4)

# 当 GPU可用时,我们可以运行以下代码
# 我们将使用 `torch.device`来将 tensor移入和移出 GPU

if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # 通过在函数中指定相应的位置参数，直接在 GPU上创建 tensor-y
    x = x.to(device)                       # 将主机端的 tensor或者使用 `.to("cuda")`方法
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # `.to`也能在移动时改变 dtype
