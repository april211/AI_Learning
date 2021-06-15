import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt


ifw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
print(ifw_people)
print(ifw_people.target_names)

X = ifw_people.data
y = ifw_people.target.reshape(-1, 1)

print(X.shape)
print(y.shape)
print(ifw_people.images.shape)

m, height, width = ifw_people.images.shape
plt.imshow(X[0].reshape(height, width))
print(X[0].shape)

plt.show()
