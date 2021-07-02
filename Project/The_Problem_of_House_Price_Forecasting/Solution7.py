import sys, os
import numpy as np
from sklearn.model_selection import train_test_split
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import NN_activators as NN_activators
import NN_Layer as NN_Layer
import NN_Loss as NN_Loss
from Neural_Network import NeuralNetwork
from sklearn.metrics import r2_score

def process_features(X):
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X = scaler.fit_transform(X)
    return X
# end


def create_layers():
    """ 构建并返回新建的神经网络的各层 """
    n_inputs = 8                    # 输入项为 8项
    n_hidden1 = 100                 # 定义包含输出层在内的三个层
    n_hidden2 = 50
    n_outputs = 1                   # 回归问题，最后一层是一个输出
    layers = []
    relu = NN_activators.ReLUActivator()
    layers.append(NN_Layer.Layer(n_inputs, n_hidden1, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden1, n_hidden2, activator=relu))
    layers.append(NN_Layer.Layer(n_hidden2, n_outputs))
    return layers
# end

housing = fetch_california_housing()
X = housing.data
y = housing.target.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

X_train = process_features(X_train)
X_test = process_features(X_test)

layers = create_layers()
loss = NN_Loss.SquaredLoss()                    # 回归问题，损失函数定义为平方损失函数

model = NeuralNetwork(layers, loss)
model.fit(X_train, y_train, 100000, 0.01)
y_pred = model.predict(X_test)

print("r2_score: {}.".format(r2_score(y_test, y_pred)))
