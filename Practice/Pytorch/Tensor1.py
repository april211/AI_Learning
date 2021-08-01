from __future__ import print_function

import torch
import numpy as np


# Returns True if obj is a PyTorch tensor.
x = torch.empty(3, 4)
print(torch.is_tensor(x))

# Returns the total number of elements in the input tensor.
print(torch.numel(x))

# Sets the default floating point dtype to d.
# default: torch.float32
torch.set_default_dtype(torch.float64)

# Get the current default floating point torch.dtype.
print(torch.get_default_dtype())

# Creates a Tensor from a numpy.ndarray
print(torch.from_numpy(np.ones((2, 3))))

# Returns a tensor filled with the scalar value 0, with the same size as input.
# xxx_like: ..., with the same size as input.
print(torch.zeros_like(x, dtype=torch.float32))

# Creates a tensor of size size filled with fill_value.
print(torch.full(size=(2, 4), fill_value=3))


