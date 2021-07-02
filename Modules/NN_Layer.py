import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from NN_activators import IdentityActivator


class Layer:
    """ 神经网络的一层（全联结） """
    def __init__(self, n_input, n_output, activator=IdentityActivator()):
        """ 
        初始化该层的神经元
        参数 n_input, n_output, activator：该层每个神经元的输入个数（即上一层神经元个数）、本层神经元个数（输出个数）、本层的激活函数
        """
        self.activator = activator                                             # 激活函数初始化
        self.b = np.zeros((n_output, 1))                                       # 该层每个神经元的偏置项初始化为 0
        rbound = np.sqrt(6.0 / (n_input + n_output))                           # 下面随机数的范围，根据实际经验所得（不能设置成零矩阵）
        self.W = np.random.uniform(-rbound, rbound, (n_output, n_input))       # Xavier初始化，实践表明对神经网络的训练十分有利
        self.outputs = np.zeros((n_output, 1))                                 # 根据该层的输出个数初始化输出
    # end

    def forward(self, inputs):
        """ 前向传播经过该层神经元时，调用此函数 """
        self.inputs = inputs                                                    # 记忆该层的神经元正向输入，j(r - 1) --> i(r)
        self.sums = self.W.dot(inputs) + self.b                                 # 计算各个神经元准备进入阈值函数的、关于该层输入的线性组合值
        self.outputs = self.activator.value(self.sums)                          # 该层的各个神经元的 sum输出经过激活函数处理，形成该层神经元的真正输出
    # end

    def back_propagation(self, delta_in, learning_rate):
        """ 反向传播经过该层时，调用此函数 """
        d = self.activator.deriative(self.sums)* delta_in                       # 该层的 delta(r) 与 sums导函数的哈达马乘积得到 d(r)
        self.delta_out = self.W.T.dot(d)                                        # delta(r-1)
        self.W_grad = d.dot(self.inputs.T)                                      # 计算损失函数关于 W的导数
        self.b_grad = d                                                         # 计算损失函数关于 b的导数
        self.W -= learning_rate* self.W_grad
        self.b -= learning_rate* self.b_grad                                    # 随机梯度下降算法，沿着梯度的反方向调整该层的模型参数
    # end
# end
