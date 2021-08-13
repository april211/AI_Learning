import math
from collections import OrderedDict

import torch
import torch.nn as nn

#---------------------------------------------------------------------#
#   DarkNet53 实现
#---------------------------------------------------------------------#

class BasicBlock(nn.Module):
    """ 
    DarkNet53 残差块数据结构 实现\n
    Structure: \n

    BasicBlock\n
      Layer1: DarknetConv2D (1* 1 Conv)\n
          -| Conv2d\n
          -| BatchNorm2d\n
          -| LeakyReLU\n
      Layer2: SAME-DarknetConv2D (3* 3 Conv)\n
          -| Conv2d\n
          -| BatchNorm2d\n
          -| LeakyReLU\n
    """
    def __init__(self, in_channels, channel_list):
        """ 
        定义残差块的网络结构：包括卷积层、标准化层、激活层等\n
        重载构造函数 | 参数：Layer1 的输入频道数、其余必须的频道参数\n
        """
        super(BasicBlock, self).__init__()                             # 继承固定写法，调用父类的构造函数初始化父类的属性

        # Layer 1：DarknetConv2D，使用 1* 1卷积，将频道数减半
        self.conv1 = nn.Conv2d(in_channels, channel_list[0], kernel_size=1,
                               stride=1, padding=0, bias=False)        # 定义一个卷积层，指定输入输出频道数、卷积核大小、步长、填充数、是否偏置
        self.bn1 = nn.BatchNorm2d(channel_list[0])                     # 批规范化层，对数据块的各通道进行 0-1特征标准化，参数为通道数目
        self.relu1 = nn.LeakyReLU(0.1)                                 # 采用 LeakyReLU激活，参数为负值时的斜率
        
        # Layer 2：SAME-DarknetConv2D，频道数翻倍（通过增加卷积核数目）
        self.conv2 = nn.Conv2d(channel_list[0], channel_list[1], kernel_size=3,
                               stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(channel_list[1])
        self.relu2 = nn.LeakyReLU(0.1)                                 # ？没有用 nn.Sequential，需要构建自己的结构
    # end

    def forward(self, x):
        """ 
        继承自父类的前向传播函数，定义了残差块网络前向传播时的行为\n
        重载前向传播 | 参数：网络输入\n
        """
        # 保存输入（残差项），对应着 ShortCut前向传播路线
        residual = x

        # MainPath前向传播
        out = self.conv1(x)                     # Layer1
        out = self.bn1(out)
        out = self.relu1(out)

        out = self.conv2(out)                   # Layer2
        out = self.bn2(out)
        out = self.relu2(out)                   # ？这里不是标准的残差块，残差在激活的后面汇入MainPath
        
        # 最终输出：MainPath + ShortCut
        out += residual
        return out
    # end
# end


class DarkNet(nn.Module):
    """ DarkNet53 特征提取网络整体的构建 """
    def __init__(self, layers):
        """ 构建 DarkNet53网络 | 参数：各层残差块的数目 """
        super(DarkNet, self).__init__()
        self.inplanes = 32                      # 定义 第一个卷积层输出的频道数目（卷积核数目）

        # 网络首先经过一个 SAME-DarknetConv2D：416,416,3 -> 416,416,32
        self.conv0 = nn.Conv2d(3, self.inplanes, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn0 = nn.BatchNorm2d(self.inplanes)
        self.relu0 = nn.LeakyReLU(0.1)

        # 下面几层是 DarkNet53的残差网络部分，使用类内自定义函数构造残差层，
        # 数据块每经过一个层，长宽每次都削减一半，频道数翻倍
        # Layer1: 416,416,32 -> 208,208,64
        self.layer1 = self._make_layer([32, 64], layers[0])

        # Layer2: 208,208,64 -> 104,104,128
        self.layer2 = self._make_layer([64, 128], layers[1])

        # Layer3: 104,104,128 -> 52,52,256
        self.layer3 = self._make_layer([128, 256], layers[2])

        # Layer4: 52,52,256 -> 26,26,512
        self.layer4 = self._make_layer([256, 512], layers[3])

        # Layer5: 26,26,512 -> 13,13,1024
        self.layer5 = self._make_layer([512, 1024], layers[4])

        # 记录 残差网络部分的各层的输出频道数目
        self.layers_out_channels = [64, 128, 256, 512, 1024]

        # 对 DarkNet53网络中的 各卷积层和批规范化层 进行 参数初始化
        for layer in self.modules():
            if isinstance(layer, nn.Conv2d):                # 卷积层（无偏置项）
                n = layer.kernel_size[0] * layer.kernel_size[1] * layer.out_channels            # 卷积核三维大小
                layer.weight.data.normal_(0, math.sqrt(2. / n))                                 # 随机化卷积核参数
            elif isinstance(layer, nn.BatchNorm2d):         # 批规范化层
                layer.weight.data.fill_(1)                  # 对应论文中的 gamma，元素个数等于该层通道数（特征数量）
                layer.bias.data.zero_()                     # 对应论文中的 beta，元素个数等于该层通道数
    # end

    def _make_layer(self, planes, blocks):
        """ 
        构建DarkNet单个主干层；\n
        每个主干层由一个 DarknetConv2D层 和 残差层（数个残差块连接） 组成；\n
        在每一个 Layer里面，首先利用一个步长为 2的 3x3卷积进行下采样，然后进行残差结构的堆叠。\n
        参数：该层的输入输出频道数、该层的残差块数\n
        """
        layers = []

        # DarknetConv2D：下采样，步长为 2，卷积核大小为 3，通道数翻倍
        layers.append(("ds_conv", nn.Conv2d(self.inplanes, planes[1], kernel_size=3,
                                stride=2, padding=1, bias=False)))
        layers.append(("ds_bn", nn.BatchNorm2d(planes[1])))
        layers.append(("ds_relu", nn.LeakyReLU(0.1)))

        # 加入残差结构
        self.inplanes = planes[1]                   # ？其他实现方式：self.inplanes必要性？
        for i in range(0, blocks):                  # https://blog.csdn.net/qq_27825451/article/details/90551513
            layers.append(("residual_{}".format(i), BasicBlock(self.inplanes, planes)))
        return nn.Sequential(OrderedDict(layers))
    # end

    def forward(self, x):
        """ 定义DarkNet53网络的前向传播行为 """
        x = self.conv0(x)
        x = self.bn0(x)
        x = self.relu0(x)

        x = self.layer1(x)
        x = self.layer2(x)
        
        # 后三个层的输出作为整个特征提取网络的输出（共 3个）
        out0 = self.layer3(x)                   # 输出：52* 52* 256
        out1 = self.layer4(out0)                # 输出：26* 26* 512
        out2 = self.layer5(out1)                # 输出：13* 13* 1024

        return out0, out1, out2
    # end
# end

def darknet53(pretrained, **kwargs):
    """ 
    获取一个标准DarkNet53网络模型，可以加载预训练的模型\n
    参数：\n
        pretrained: 预训练模型路径\n
        kwargs: else\n
    """
    model = DarkNet([1, 2, 8, 8, 4])            # 获得一个 DarkNet53网络对象
    if pretrained:
        if isinstance(pretrained, str):
            model.load_state_dict(torch.load(pretrained))       # 加载预训练模型，并将其参数配置给当前模型
        else:
            raise Exception("darknet request a pretrained path. got [{}]".format(pretrained))
    return model
# end
