import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
import PCA as pca
import PCA_Kernel as pcak

def rbf_kernel(x1, x2):
    """径向基核函数（高斯核函数） x1, x2: vector"""
    sigma = 0.3
    return np.exp(-(1.0 / sigma)* np.linalg.norm(x1-x2, 2)** 2)
# end

def linear_kernel(x1, x2):
    """ 线性核函数 """
    c = 5.0
    return np.dot(x1.reshape(1, -1), x2.reshape(-1, 1)) + c
# end


X, y = make_circles(n_samples=400, factor=0.3, noise=0.05)
y = y.reshape(-1, 1)

model1 = pca.PCA(n_components=1)
Z1 = model1.fit_transform(X)

model2 = pcak.PCA_Kernel(n_components=1, kernel=rbf_kernel)
Z2 = model2.fit_transform(X)


Horizon1 = np.ones(Z1.shape)
Horizon2 = np.ones(Z2.shape)

plt.style.use('seaborn-darkgrid')
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].scatter(Z1[:,0], Horizon1[:,0], c=list(y), cmap=plt.cm.plasma, edgecolors='none', s=5)
axes[1].scatter(Z2[:,0], Horizon2[:,0], c=list(y), cmap=plt.cm.plasma, edgecolors='none', s=5)
axes[0].axis('off')
axes[1].axis('off')

plt.show()
