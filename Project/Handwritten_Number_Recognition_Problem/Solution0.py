import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from tensorflow.examples.tutorials.mnist import input_data
import Softmax_Regression_SGD as srsgd
import Classification_Metrics as cm


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
X_train, Y_train = mnist.train.images, mnist.train.labels
X_test, Y_test = mnist.test.images, mnist.test.labels

model = srsgd.SoftmaxRegressionSGD()
model.fit(X_train, Y_train, eta_0=50, eta_1=100, N=100000)
proba = model.predict_proba(X_test)
accuracy = cm.accuracy_score(np.argmax(Y_test, axis=1), np.argmax(proba, axis=1))

print("Accuracy = {}.".format(accuracy))
