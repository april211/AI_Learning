import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from Decision_Tree_Classifier import DecisionTreeClassifier


def get_data():
    """ 从本地 csv 文件中读入数据 """
    df = pd.read_csv("Project\\Speech_Recognition_Problem\\voice.csv")
    y = (df['label'].values=='male').astype(np.int64)
    df.drop('label', 1, inplace=True)
    X = df.values
    return X, y.reshape(-1, 1)
# end


X, y = get_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train).toarray()

model = DecisionTreeClassifier(max_depth=2)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy = {}.".format(accuracy))
