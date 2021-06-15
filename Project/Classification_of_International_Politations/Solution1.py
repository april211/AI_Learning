import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
import SVM_SMO_SOFT_KERNEL as svm_soft_kernel


def linear_kernel(x1, x2):
    """ 线性核函数 """
    c = 5.0
    return np.dot(x1.reshape(1, -1), x2.reshape(-1, 1)) + c


ifw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
names = ifw_people.target_names

X = ifw_people.data
y = ifw_people["target"].reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)

idk = 10
Xp_test = X_test[idk]
yp_test = y_test[idk]
name_p = names[yp_test]

print("Answer", name_p)

for i in range(7):
    y_train_i = 2* (y_train==i).astype(np.int64).reshape(-1, 1) - 1
    model = svm_soft_kernel.SoftKernelSVM(C=4.0, kernel=linear_kernel)
    model.fit(X_train, y_train_i, N=8)
    y_pred = model.predict(Xp_test.reshape(1, -1))
    if(y_pred[0] == 1):
        print("Yes", names[i], y_pred)
    else:
        print("No", names[i], y_pred)
