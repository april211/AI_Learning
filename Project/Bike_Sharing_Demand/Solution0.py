import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import pandas as pd
from sklearn.model_selection import train_test_split
from Decision_Tree_Regressor import DecisionTreeRegressor
from sklearn.metrics import r2_score


def get_data():
    """ 从本地 csv 文件中读入数据 """
    df = pd.read_csv("Project\\Bike_Sharing_Demand\\bike.csv")
    df.datetime = df.datetime.apply(pd.to_datetime)
    df['hour'] = df.datetime.apply(lambda x:x.hour)
    y = df['count'].values
    df.drop(['datetime', 'casual', 'registered', 'count'], axis=1, inplace=True)
    X = df.values
    return X, y
# end

X, y = get_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

model = DecisionTreeRegressor(max_depth=2)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("r2 = {}.".format(r2_score(y_test, y_pred)))