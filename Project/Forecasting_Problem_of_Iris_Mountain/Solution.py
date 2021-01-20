import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Perceptron_Class import Perceptron


iris = datasets.load_iris()
X = iris["data"][:, (0, 1)]
y = 2* (iris["target"] == 0).astype(np.int) - 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

model = Perceptron()
model.fit(X_train, y_train)
model.predict(X_test)

plt.style.use('seaborn-darkgrid')
fig, axs = plt.subplots(1, 2, figsize=(9, 4))  # a figure with a 1x2 grid of Axes
axs[0].scatter(X_train[:,0], X_train[:,1], c=list(y_train), cmap=plt.cm.seismic, edgecolors='none', s=2)
axs[1].scatter(X_test[:,0], X_test[:,1], c=list(y_test), cmap=plt.cm.seismic, edgecolors='none', s=2)

LX1 = np.linspace(4.0, 8.0, 100)
LX2 = ((-1.0)* (model.w[0])* LX1 - model.b) / (model.w[1])
axs[0].plot(LX1, LX2, linewidth=1)
axs[1].plot(LX1, LX2, linewidth=1)

plt.show()
