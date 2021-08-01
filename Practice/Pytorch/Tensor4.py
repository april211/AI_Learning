import torch

x = torch.tensor([(1, 2), (2, 3), (3, 4)])      # 圆括号化成方括号处理

print(x.shape)
print(x)

a = x.index_select(1, torch.tensor([0]))        # the second parameter has to be a Tenor
print(a)

b = x.index_select(1, torch.tensor([1]))
print(b)

# repeat() behaves differently from numpy.repeat, but is more similar to numpy.tile.
# sizes (torch.Size or int...) – The number of times to repeat this tensor along each dimension
print(a.repeat(2, 1))           # H(axis=0), W(axis=1)
print(a.repeat(1, 2))           # H(axis=0), W(axis=1)
print(a.repeat(2, 1, 1))        # C(axis=2), H(axis=0), W(axis=1)
print(a.repeat(2, 1).repeat(1, 1, 4))
print(a.repeat(1, 2, 4))


# https://pytorch.org/docs/stable/generated/torch.Tensor.repeat.html
