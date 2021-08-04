import torch
import torch.nn as nn


mContainer = nn.ModuleList([nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1, bias=False),
                    nn.Conv2d(53, 30, kernel_size=1, stride=1, padding=0, bias=False)])

layer_list = list(mContainer)

print(layer_list[0](torch.randn((1, 3, 7, 7))))
