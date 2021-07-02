import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from tensorflow.examples.tutorials.mnist import input_data
import NN_activators as NN_activators
import NN_Layer as NN_Layer
import NN_Loss as NN_Loss
from Neural_Network import NeuralNetwork
from sklearn.metrics import accuracy_score


def create_layers():
    """ 构建并返回新建的神经网络的各层 """
    n_features = 28* 28                    # 与手写图片尺寸相对应
    n_hidden1 = 300                        # 定义包含输出层在内的三个层
    n_hidden2 = 100
    n_classes = 10                         # 数字分类问题，最后一层是 10个输出
    layers = []
    relu = NN_activators.ReLUActivator()
    layers.append(NN_Layer.Layer(n_features, n_hidden1, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden1, n_hidden2, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden2, n_classes))
    return layers
# end


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
X_train, Y_train = mnist.train.images, mnist.train.labels
X_test, Y_test = mnist.test.images, mnist.test.labels

layers = create_layers()
loss = NN_Loss.LogarithmicLoss()

model = NeuralNetwork(layers, loss)
model.fit(X_train, Y_train, 50000, 0.01)
V = model.predict(X_test)                       # 输出的是由 OneHot向量构成的矩阵

PROBA = NN_Loss.softmax(V)                      # 得到 softmax矩阵
y_pred = np.argmax(PROBA, axis=1)

accuracy = accuracy_score(np.argmax(Y_test, axis=1), y_pred)
print("accuracy: {}.".format(accuracy))
