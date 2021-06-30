import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from Random_Forest_Classifier import RandomForestClassifier
from Decision_Tree_Classifier import DecisionTreeClassifier



X, y = make_moons(n_samples=1000, noise=0.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train.reshape(-1, 1)).toarray()

tree = DecisionTreeClassifier(max_depth=5)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

print("Tree accuracy = {}.".format(accuracy_score(y_test, y_pred)))


forest = RandomForestClassifier(max_depth=2, num_trees=200, 
                                feature_sample_rate=0.5, data_sample_rate=0.25)
forest.fit(X_train, y_train)
y_pred = forest.predict(X_test)

print("Random forest accuracy = {}.".format(accuracy_score(y_test, y_pred)))
