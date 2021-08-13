from collections import OrderedDict

import torch
import torch.nn as nn

from nets.darknet import darknet53

#------------------------------------------------------------------------#
#   YOLOv3 实现
#------------------------------------------------------------------------#

def conv2d(in_channels, out_channels, kernel_size):
    """
    构建 DarknetConv2D 结构：\n
    conv2d\n
        -| nn.Conv2d, stride=1, bias=False\n
        -| nn.BatchNorm2d\n
        -| nn.LeakyReLU\n
    此函数创建的 DarknetConv2D层 并不改变张量的宽和高。\n
    功能解析：\n
        kernel_size == 1, padding == 0, (1* 1) Conv, 相当于：SAME;\n
        kernel_size == 3, padding == 1, (3* 3) Conv, 相当于：SAME;\n
    注意：在接下来的应用中，kernel_size 只可能等于 1 或 3 这两个值。\n
    """
    padding = (kernel_size - 1) // 2 if kernel_size else 0               # ？kernel_size < 0，这里 padding == 0 or 1
    return nn.Sequential(OrderedDict([
        ("conv", nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=1, padding=padding, bias=False)),
        ("bn", nn.BatchNorm2d(out_channels)),
        ("relu", nn.LeakyReLU(0.1)),
    ]))
# end

#------------------------------------------------------------------------#
#   make_last_layers里面一共有 7个卷积，前 5个用于提取特征。
#   后 2个用于获得yolo网络的预测结果
#------------------------------------------------------------------------#
def make_last_layers(channel_list, in_channels, out_channels):
    """
    构建YOLO的输出端网络：\n
        实现          <--->    原文结构          作用\n
    DarknetConv2D X 5 <---> Conv2D Block 5L   特征提取\n
    DarknetConv2D X 1 <---> Conv2D 3* 3       预测结果\n
    nn.Conv2d     X 1 <---> Conv2D 1* 1       预测结果\n
    （后2层合称为 'Yolo Head'）\n
    共计：7层
    """
    mContainer = nn.ModuleList([
        # ？5次特征震荡卷积处理部分（对应结构图中的 5L）
        conv2d(in_channels, channel_list[0], 1),                # 1* 1 Conv, channel数下降
        conv2d(channel_list[0], channel_list[1], 3),            # 3* 3 Conv, channel数上升
        conv2d(channel_list[1], channel_list[0], 1),            # 1* 1 Conv, channel数下降
        conv2d(channel_list[0], channel_list[1], 3),            # 3* 3 Conv, channel数上升
        conv2d(channel_list[1], channel_list[0], 1),            # 1* 1 Conv, channel数下降

        # Yolo Head部分，对应红色框
        conv2d(channel_list[0], channel_list[1], 3),                        # 3* 3 Conv, channel数上升
        nn.Conv2d(channel_list[1], out_channels, kernel_size=1,             # 1* 1 Conv, channel数降至目标输出数目
                                        stride=1, padding=0, bias=True)
    ])
    return mContainer
# end

class YoloBody(nn.Module):
    """ YOLOv3 网络实现 """
    def __init__(self, anchor, num_classes):
        """ 
        YOLOv3 网络结构初始化\n
        """
        super(YoloBody, self).__init__()
        #---------------------------------------------------#   
        #   生成 darknet53的主干模型。
        #   从 darknet53网络输出中，获得三个有效特征层。
        #   他们的 shape分别是：
        #   52,52,256
        #   26,26,512
        #   13,13,1024
        #---------------------------------------------------#
        self.backbone = darknet53(None)                                    # 默认不装载任何预训练模型

        # backbone_out_channels : [64, 128, 256, 512, 1024]
        backbone_out_channels = self.backbone.layers_out_channels

        # 特征金字塔采样并输出
        # 网络输出：13* 13* final_out_channel0
        final_out_channel0 = len(anchor[0]) * (5 + num_classes)                     # 单个 grid cell 最多可侦测 len(anchor[0])个物体
        self.final_layer0 = make_last_layers([512, 1024], backbone_out_channels[-1], 
                                        final_out_channel0)        # channels: 1024 --> final_out_channel0; 不需要 concat

        # 网络输出：26* 26* final_out_channel1
        self.layer1_conv = conv2d(512, 256, 1)                                      # 1* 1 Conv, 13* 13* 512 --> 13* 13* 256
        self.layer1_upsample = nn.Upsample(scale_factor=2, mode='nearest')          # 上采样：13* 13* 256 --> 26* 26* 256
        final_out_channel1 = len(anchor[1]) * (5 + num_classes)
        self.final_layer1 = make_last_layers([256, 512], backbone_out_channels[-2] + 256, 
                                        final_out_channel1)        # channels: 768 --> final_out_channel1; 768 是经过 concat后的尺寸
        
        # 网络输出：52* 52* final_out_channel2
        self.layer2_conv = conv2d(256, 128, 1)
        self.layer2_upsample = nn.Upsample(scale_factor=2, mode='nearest')
        final_out_channel2 = len(anchor[2]) * (5 + num_classes)
        self.final_layer2 = make_last_layers([128, 256], backbone_out_channels[-3] + 128, 
                                        final_out_channel2)        # channels: 384 --> final_out_channel2; 384 是经过 concat后的尺寸
    # end

    def forward(self, x):
        """
        YOLOv3 前向传播
        """
        def _branch(final_layer, layer_input):
            """
            金字塔特征提取分支\n
            参数：5L + Head层、输入数据\n
            返回：最终结果（作为模型输出）、中途分支（准备卷积上采样）\n
            """
            layer_list = list(final_layer)                              # 遍历 ModuleList中的网络，手动逐层 forward

            # 5L特征提取结束，分支，准备卷积上采样
            layer_input = layer_list[0](layer_input)                    
            layer_input = layer_list[1](layer_input)
            layer_input = layer_list[2](layer_input)
            layer_input = layer_list[3](layer_input)
            layer_input = layer_list[4](layer_input)
            out_branch = layer_input                                    # 找个变量记录一下，就算分支了
            layer_input = layer_list[5](layer_input)
            layer_input = layer_list[6](layer_input)
            return layer_input, out_branch                              # layer_input 是经过整个7层的，out_branch只经过了前五层
        # end
        
        #---------------------------------------------------#   
        #   获得三个来自 DarkNet53的有效特征输出
        #   52,52,256；26,26,512；13,13,1024
        #---------------------------------------------------#
        feature2, feature1, feature0 = self.backbone(x)

        #---------------------------------------------------#
        #   第一个特征层
        #   out0 = (batch_size,255,13,13)
        #---------------------------------------------------#
        # out0_branch: (5L) 13,13,1024 -> 13,13,512 -> 13,13,1024 -> 13,13,512 -> 13,13,1024 -> 13,13,512
        # out0: (5L) -> 13* 13* 1024 -> 13* 13* final_out_channel0
        out0, out0_branch = _branch(self.final_layer0, feature0)

        # out0_branch 分支卷积 &上采样：13,13,512 -> 13,13,256 -> 26,26,256 (x1)
        x1 = self.layer1_conv(out0_branch)               
        x1 = self.layer1_upsample(x1)

        # concat: 26,26,256 + 26,26,512 -> 26,26,768 (x1)
        x1 = torch.cat([x1, feature1], 1)

        #---------------------------------------------------#
        #   第二个特征层
        #   out1 = (batch_size,255,26,26)
        #---------------------------------------------------#
        # out1_branch: (5L) 26,26,768 -> 26,26,256 -> 26,26,512 -> 26,26,256 -> 26,26,512 -> 26,26,256
        # out1: (5L) -> 26,26,512 -> 26,26,final_out_channel1
        out1, out1_branch = _branch(self.final_layer1, x1)

        # out1_branch 分支卷积 &上采样：26,26,256 -> 26,26,128 -> 52,52,128 (x2)
        x2 = self.layer2_conv(out1_branch)
        x2 = self.layer2_upsample(x2)

        # concat: 52,52,128 + 52,52,256 -> 52,52,384 (x2)
        x2 = torch.cat([x2, feature2], 1)

        #---------------------------------------------------#
        #   第三个特征层
        #   out2 = (batch_size,255,52,52)
        #---------------------------------------------------#
        # 52,52,384 -> 52,52,128 -> 52,52,256 -> 52,52,128 -> 52,52,256 -> 52,52,128
        out2, _ = _branch(self.final_layer2, x2)
        return out0, out1, out2
        # OUTPUT ATTENTION: 
        # PyTorch modules dealing with image data require tensors to be laid out as C × H × W : 
        # channels, height, and width, respectively. 
    # end
# end
