import sys, os
import numpy as np
import pandas as pd
sys.path.append(os.getcwd() + r'\Modules')
import NN_activators as NN_activators
import NN_Layer as NN_Layer
import NN_Loss as NN_Loss
from Neural_Network import NeuralNetwork
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def get_data():
    df = pd.read_csv("Project\\Fashion_Category_Recognition\\fashion-mnist_train.csv")
    y = df['label'].values
    df.drop(['label'], 1, inplace=True)
    X = df.values
    return X, y.reshape(-1, 1)                  # 此时返回的标签向量 y是一个数值标签向量
# end

def create_layers():
    """ 构建并返回新建的神经网络的各层 """
    n_features = 28* 28                    # 输入特征数与时装灰度图片尺寸（28* 28）相对应
    n_hidden1 = 300                        # 第一隐层：300
    n_hidden2 = 100                        # 第二隐层：100
    n_hidden3 = 40                         # 第三隐层：40
    n_classes = 10                         # 输出层：0 ~ 9，共计 10类
    layers = []
    relu = NN_activators.ReLUActivator()            # 获得 ReLU激活函数
    ide = NN_activators.IdentityActivator()         # 获得 Identity激活函数
    layers.append(NN_Layer.Layer(n_features, n_hidden1, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden1, n_hidden2, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden2, n_hidden3, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden3, n_classes, activator=ide))
    return layers
# end



X, y = get_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

encoder = MinMaxScaler()
X_train = encoder.fit_transform(X_train)
X_test = encoder.fit_transform(X_test)

encoder = OneHotEncoder()
Y_train = encoder.fit_transform(y_train)                # 仅将训练数据集的标签转换成 OneHot向量构成的矩阵

layers = create_layers()
loss = NN_Loss.LogarithmicLoss()                        # 分类问题，使用对数损失函数（目标函数为交叉熵）

model = NeuralNetwork(layers, loss)
model.fit(X_train, Y_train, 70000, 0.02)
VR = model.predict(X_test)                              # 注意：输出的是与 OneHot向量同维度的一个矩阵（一个测试点对应一个 OneHot向量），可能不符合概率要求

PROBA = NN_Loss.softmax(VR)                             # V(R)矩阵需要经过 Softmax变换，得到 softmax矩阵，符合概率要求
y_pred = np.argmax(PROBA, axis=1)                       # 最大分类函数，取预测概率最大的一个类别作为最终预测结果（一个数值，0 ~ 9）

accuracy = accuracy_score(y_test, y_pred)               # 计算准确率
print("accuracy: {}.".format(accuracy))
