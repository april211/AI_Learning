import sys, os
import numpy as np
import pandas as pd
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from Decision_Tree_Classifier import DecisionTreeClassifier
from Random_Forest_Classifier import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score


def get_data():
    df = pd.read_csv("Project\\Income_Predict\\adult.csv")
    y = (df['income'].values=='>50K').astype(np.int64)                            # 薪资>50K的，标签为 1
    df['clean'] = df['capital-gain'] - df['capital-loss']                         # 相关特征归并
    hocc_set = {'Craft-repair', 'Exec-managerial', 'Prof-specialty', 'Machine-op-inspct', 'Protective-serv', 'Sales', 'Transport-moving'}        # 可能的高收入人群职业
    for i in range(len(df['occupation'].values)):
        if df['occupation'].values[i] in hocc_set:
            df['occupation'].values[i] = 1
        else:
            df['occupation'].values[i] = -1
    df.drop(['capital-gain', 'capital-loss', 'income', 'workclass', 'education', 'marital-status',
            'relationship', 'race', 'gender', 'native-country', 'fnlwgt', 'age'], axis=1, inplace=True)
    X = df.values
    print(df)
    return X, y.reshape(-1, 1)
# end

X, y = get_data()
print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train).toarray()

tree = DecisionTreeClassifier(max_depth=10)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

print("Tree accuracy = {}.".format(accuracy_score(y_test, y_pred)))


forest = RandomForestClassifier(max_depth=10, num_trees=100, 
                                feature_sample_rate=0.75, data_sample_rate=0.01, random_state=42)
forest.fit(X_train, y_train)
y_pred = forest.predict(X_test)

print("Random Forest accuracy = {}.".format(accuracy_score(y_test, y_pred)))


# http://archive.ics.uci.edu/ml/datasets/Adult
