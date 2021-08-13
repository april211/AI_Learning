import onnx
from onnx import numpy_helper
import torch
import numpy as np
from yolo3 import YoloBody


def get_anchors(anchors_path):
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape([-1, 3, 2])[::-1, :, :]



num_classes = 3
anchors_path = 'Practice\Pytorch\EPT\yolo_anchors.txt'
anchors      = get_anchors(anchors_path)


model = YoloBody(anchors, num_classes)

onnx_model = onnx.load('Practice\Pytorch\EPT\Yolov3_55.onnx')

graph = onnx_model.graph
initalizers = dict()

for init in graph.initializer:
    initalizers[init.name] = numpy_helper.to_array(init)

for name, p in model.named_parameters():
    p.data = (torch.from_numpy(initalizers[name])).data

torch.save(model.state_dict(), '999.pth')
