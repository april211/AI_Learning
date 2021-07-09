import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import PCA as pca
import PCA_Kernel as pcak

def rbf_kernel(x1, x2):
    """径向基核函数（高斯核函数） x1, x2: vector"""
    sigma = 4.0
    return np.exp((-1.0 / (2.0* (sigma**2)))* np.linalg.norm(x1-x2, ord=2)** 2)
# end

def linear_kernel(x1, x2):
    """ 线性核函数 """
    c = 5.0
    return np.dot(x1.reshape(1, -1), x2.reshape(-1, 1)) + c
# end

iris = datasets.load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

model1 = pca.PCA(n_components=2)
Z1 = model1.fit_transform(X)

model2 = pcak.PCA_Kernel(n_components=2, kernel=rbf_kernel)
Z2 = model2.fit_transform(X)


plt.style.use('seaborn-darkgrid')
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].scatter(Z1[:,0], Z1[:,1], c=list(y), cmap=plt.cm.plasma, edgecolors='none', s=6)
axes[1].scatter(Z2[:,0], Z2[:,1], c=list(y), cmap=plt.cm.plasma, edgecolors='none', s=6)
plt.show()
