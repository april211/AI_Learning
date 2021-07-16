import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from DBSCAN import DBSCAN
from AgglomerativeClustering import AgglomerativeClustering



X, y = make_blobs(n_samples=300, centers=3,
                  random_state=0, cluster_std=0.8)

model1 = DBSCAN(eps=0.6, min_sample=5)
assignments1 = model1.fit_transform(X)

model2 = AgglomerativeClustering(n_clusters=3)
_, assignments2 = model2.fit_transform(X)

plt.figure(1)
plt.scatter(X[:, 0], X[:, 1], c=assignments1)

plt.figure(2)
plt.scatter(X[:, 0], X[:, 1], c=assignments2)
plt.show()
