import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from K_means import K_Means
from DBSCAN import DBSCAN
from AgglomerativeClustering import AgglomerativeClustering
from sklearn.metrics import v_measure_score


iris = datasets.load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

model1 = K_Means(n_clusters=3, max_iter=500, random_state=0)
_, assignments1 = model1.fit_transform(X)

model2 = AgglomerativeClustering(n_clusters=3)
_, assignments2 = model2.fit_transform(X)

model3 = DBSCAN(eps=0.6, min_sample=5)
assignments3 = model3.fit_transform(X)

y = list(y.flatten())
assignments1 = list(assignments1.flatten())
assignments2 = list(assignments2.flatten())
assignments3 = list(assignments3.flatten())

h1 = v_measure_score(y, assignments1)
h2 = v_measure_score(y, assignments2)
h3 = v_measure_score(y, assignments3)

# 使用  V-measure score 评估模型预测与样本原标签的符合程度，其值越接近 1代表越相符，模型表现越好
print("K_Means's V-measure score: {}.".format(h1))
print("AgglomerativeClustering V-measure score: {}.".format(h2))
print("DBSCAN V-measure score: {}.".format(h3))
