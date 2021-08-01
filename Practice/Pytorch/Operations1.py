from __future__ import print_function

import torch

# Concatenates the given sequence of seq tensors in the given dimension. All tensors must either have the same shape (except in the concatenating dimension) or be empty.
x = torch.randn(2, 3)
print(torch.cat((x, x, x), dim=0))
print(torch.cat((x, x), dim=1))

# Splits a tensor into a specific number of chunks. Each chunk is a view of the input tensor.
# Last chunk will be smaller if the tensor size along the given dimension dim is not divisible by chunks.
print(torch.chunk(x, 2, dim=1))
