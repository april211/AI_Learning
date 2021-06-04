import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import Softmax_Regression_SGD as srsgd
import Classification_Metrics as cm
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
from skimage import io
from skimage.color import rgb2gray
from skimage import filters


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
X_train, Y_train = mnist.train.images, mnist.train.labels
X_test, Y_test = mnist.test.images, mnist.test.labels

X_train_m, X_train_n = X_train.shape
X_test_m, X_test_n = X_test.shape

# 对MNIST数据使用 isodata阈值方法进行二值化
for i in range(X_train_m):
    x_gray = X_train[i, :].reshape(28, 28)
    thx = filters.threshold_isodata(x_gray)
    X_train[i, :] = ((x_gray > thx).astype(np.int64) == 0).astype(np.int64).reshape(1, 784)

for i in range(X_test_m):
    x_gray = X_test[i, :].reshape(28, 28)
    thx = filters.threshold_isodata(x_gray)
    X_test[i, :] = ((x_gray > thx).astype(np.int64) == 0).astype(np.int64).reshape(1, 784)

model = srsgd.SoftmaxRegressionSGD()
model.fit(X_train, Y_train, eta_0=50, eta_1=100, N=100000)
proba = model.predict_proba(X_test)
accuracy = cm.accuracy_score(np.argmax(Y_test, axis=1), np.argmax(proba, axis=1))

print("Accuracy = {}.".format(accuracy))


img = io.imread("Project\\Handwritten_Number_Recognition_Problem\\A22.jpg")
img_gray = rgb2gray(img)
thresh = filters.threshold_isodata(img_gray)

img_bin_x = ((img_gray > thresh).astype(np.int64) == 1).astype(np.int64).reshape(1, 784)
# plt.imshow(X_train[2, :].reshape(28, 28), cmap='gray')
plt.imshow(img_bin_x.reshape(28, 28), cmap='gray')
plt.show()

y_pred = model.predict(img_bin_x)
print("The prediction of my number: {}.".format(y_pred))
