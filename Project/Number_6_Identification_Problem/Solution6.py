import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from tensorflow.examples.tutorials.mnist import input_data
import Logistic_Regression_L1_SubGD as lrl1
import Classification_Metrics as cm
import matplotlib.pyplot as plt
import ROC as roc


def threshold(t, proba):
    """ 阈值分类函数的实现 """
    return (proba >= t).astype(np.int)
# end

def plot_precision_recall_curve(proba, y):
    """ 绘制精确率和召回率随着阈值变化的曲线 """
    iter_cnt = 50
    precision = np.array([])
    recall = np.array([])
    thresh = np.array([])
    for i in range(iter_cnt):
        z = threshold((1.0 / iter_cnt)* i, proba)
        tp = (y* z).sum()
        fp = ((1 - y)* z).sum()
        fn = (y* (1 - z)).sum()
        thresh = np.append(thresh, (1.0 / iter_cnt)* i)
        precision = np.append(precision, 1.0* (tp / (tp + fp)))
        recall = np.append(recall, 1.0* (tp / (tp + fn)))
    plt.title("Precision-Recall-Threshold Curve")
    plt.xlabel("Threshold")
    plt.ylabel("Ratio")
    plt.plot(thresh, precision, label="Precision")
    plt.plot(thresh, recall, label="Recall")
    plt.legend()
# end

def plot_roc_curve(proba, y):
    """ 绘制ROC曲线 """
    iter_cnt = 50
    fpr = np.array([])
    tpr = np.array([]) 
    for i in range(iter_cnt):
        z = threshold((1.0 / iter_cnt)* i, proba)
        tp = (y* z).sum()
        fp = ((1 - y)* z).sum()
        tn = ((1 - y)* (1 - z)).sum()
        fn = (y* (1 - z)).sum()
        fpr = np.append(fpr, 1.0* (fp / (fp + tn)))
        tpr = np.append(tpr, 1.0* (tp / (tp + fn)))
    plt.title("ROC")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.plot(fpr, tpr)
    return fpr, tpr


mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)
X_train, y_train = mnist.train.images, mnist.train.labels
X_test, y_test = mnist.test.images, mnist.test.labels
y_train = (y_train==5).astype(np.int).reshape(-1, 1)
y_test = (y_test==5).astype(np.int).reshape(-1, 1)

model = lrl1.LogisticRegressionL1GD(Lambda=0.1)
model.fit(X_train, y_train, eta=0.08, N=200)

proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)

precision = cm.precision_score(y_test, y_pred)
recall = cm.recall_score(y_test, y_pred)

print("Precision: {}.".format(precision))
print("Recall: {}.".format(recall))

plt.figure(1)
plot_precision_recall_curve(proba, y_test)

aoc_list = []

model.fit(X_train, y_train, eta=0.08, N=20)
proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
plt.figure(2)
fpr, tpr = roc.plot_roc_curve(proba, y_test)
aoc_list.append("AOC when N=20: {}.".format(np.trapz(np.flip(tpr), np.flip(fpr))))

model.fit(X_train, y_train, eta=0.08, N=100)
proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
plt.figure(3)
fpr, tpr = roc.plot_roc_curve(proba, y_test)
aoc_list.append("AOC when N=100: {}.".format(np.trapz(np.flip(tpr), np.flip(fpr))))

model.fit(X_train, y_train, eta=0.08, N=200)
proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
plt.figure(4)
fpr, tpr = roc.plot_roc_curve(proba, y_test)
aoc_list.append("AOC when N=200: {}.".format(np.trapz(np.flip(tpr), np.flip(fpr))))

model.fit(X_train, y_train, eta=0.08, N=1000)
proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
plt.figure(5)
fpr, tpr = roc.plot_roc_curve(proba, y_test)
aoc_list.append("AOC when N=1000: {}.".format(np.trapz(np.flip(tpr), np.flip(fpr))))
plt.show()

for str in aoc_list:
    print(str)
