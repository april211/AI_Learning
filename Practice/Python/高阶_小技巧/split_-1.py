import numpy as np


anchors = "10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326"
anchors = [float(x) for x in anchors.split(',')]
print(anchors)
print(np.array(anchors).reshape([-1, 3, 2])[::-1,:,:])

# https://blog.csdn.net/mingyuli/article/details/81604795
