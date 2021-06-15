import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
import SVM_SMO_SOFT_KERNEL as svm_soft_kernel
import matplotlib.pyplot as plt
import Classification_Metrics as cm


def rbf_kernel(x1, x2):
    """径向基核函数（高斯核函数） x1, x2: vector"""
    sigma = 4.0
    return np.exp((-1.0 / (2.0* (sigma**2)))* np.linalg.norm(x1-x2, ord=2)** 2)
# end

def linear_kernel(x1, x2):
    """ 线性核函数 """
    c = 5.0
    return np.dot(x1.reshape(1, -1), x2.reshape(-1, 1)) + c



ifw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
names = ifw_people.target_names

X = ifw_people.data
y = 2* (ifw_people["target"]==3).astype(np.int64).reshape(-1, 1) - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)

model = svm_soft_kernel.SoftKernelSVM(C=4.0, kernel=linear_kernel)
model.fit(X_train, y_train, N=11)

y_pred = model.predict(X_test)

y_pred = (y_pred==1).astype(np.int64).reshape(-1, 1)
y_test = (y_test==1).astype(np.int64).reshape(-1, 1)
recall = cm.recall_score(y_test, y_pred)
precision = cm.precision_score(y_test, y_pred)

print("recall = {}".format(recall))
print("precision = {}".format(precision))
