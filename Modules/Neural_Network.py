import numpy as np


class NeuralNetwork:
    def __init__(self, layers, loss):
        """ 初始化各神经元层和此神经网络的损失函数 """
        self.layers = layers
        self.loss = loss
    # end

    def forward(self, x):
        """ 神经网络前向传播 """
        layers = self.layers
        inputs = x
        for layer in layers:                # 每一次迭代，向前一层
            layer.forward(inputs)
            inputs = layer.outputs          # 该层的输入作为下一层的输出
        return inputs                       # 最后一层的输出就是该神经网络的输出
    # end

    def back_propagation(self, y, outputs, learning_rate):
        """ 神经网络反向传播 """
        delta_in = self.loss.deriative(y, outputs)              # 根据神经网络的实际输出和样本标签值来计算损失函数对输出的一阶导数
        for layer in self.layers[::-1]:
            layer.back_propagation(delta_in, learning_rate)
            delta_in = layer.delta_out                          # delta(r) -(阈值函数导数)-> d(r) -(W.T)-> delta(r-1)
    # end

    def fit(self, X, y, N, learning_rate):
        """ 训练函数 N: 训练轮数 learning_rate: 学习速率 """
        for t in range(N):
            i = np.random.randint(0, len(X))                    # 随机梯度下降算法要求随机选中一个样本
            outputs = self.forward(X[i].reshape(-1, 1))         # 计算该样本的预测值
            self.back_propagation(y[i].reshape(-1, 1), outputs, learning_rate)      # 根据此次的输出和对应的标签值，执行反向传播算法
    # end

    def predict(self, X):
        """ 预测函数 """
        y = []
        for i in range(len(X)):                                 # 遍历输入矩阵中的样本向量，逐个放入神经网络中预测
            v = self.forward(X[i].reshape(-1, 1)).reshape(-1)   # 注意：该预测值是一个数组，尚未经过 Softmax处理，是一个通用的输出
            y.append(v)
        return np.array(y)                                      # 整合成 numpy数组矩阵
    # end
# end
