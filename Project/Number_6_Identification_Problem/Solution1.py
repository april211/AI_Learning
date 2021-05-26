import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from tensorflow.examples.tutorials.mnist import input_data
import Logistic_Regression_L1_SubGD as lrl1
import Classification_Metrics as cm

# 这个算法耗时过长

mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)
X_train, y_train = mnist.train.images, mnist.train.labels
X_test, y_test = mnist.test.images, mnist.test.labels
y_train = (y_train==6).astype(np.int).reshape(-1, 1)
y_test = (y_test==6).astype(np.int).reshape(-1, 1)

model = lrl1.LogisticRegressionL1GD(Lambda=0.2)
model.fit(X_train, y_train, eta=0.02, N=1)
proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
entropy = model.cross_entropy(y_test, proba)
accuracy = cm.accuracy_score(y_test, y_pred)

print("Cross entropy = {}.".format(entropy))
print("Accuracy = {}.".format(accuracy))
