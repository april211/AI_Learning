import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

print(iris.feature_names)
print(iris.target_names)
print(iris.data)
print(iris.target)
