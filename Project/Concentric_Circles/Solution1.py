import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
import DBSCAN as db
import K_means as km


np.random.seed(0)        
X, y = make_circles(n_samples=400, factor=.3, noise=.05)

dbscan = db.DBSCAN(eps = 0.5, min_sample = 5)
db_assignments = dbscan.fit_transform(X)
kmeans = km.K_Means(n_clusters = 2)
km_centers, km_assignments = kmeans.fit_transform(X)

plt.figure(20)
plt.scatter(X[:, 0], X[:,1], c = db_assignments)
plt.figure(21)
plt.scatter(X[:, 0], X[:,1], c = km_assignments)
plt.show()
