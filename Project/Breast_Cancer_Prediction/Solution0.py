import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
import Logistic_Regression_SGD as lrsgd
import Classification_Metrics as cm
import ROC as roc


def process_features(X):
    """ 数据标准化、加 1列 """
    m, n = X.shape
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X = np.c_[np.ones((m, 1)), X]
    return X


X, y = load_breast_cancer(return_X_y=True)
X = process_features(X)
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = lrsgd.LogisticRegressionSGD()
model.fit(X_train, y_train, eta_0=10, eta_1=50, N=7000)

proba = model.predict_proba(X_test)
ce = cm.cross_entropy(y_test, proba)

y_pred = model.predict(X_test)
accuracy = cm.accuracy_score(y_test, y_pred)
precision = cm.precision_score(y_test, y_pred)
recall = cm.recall_score(y_test, y_pred)

print("Cross Entropy: {}.".format(ce))
print("Accuracy: {}.".format(accuracy))
print("Precision: {}.".format(precision))
print("Recall: {}.".format(recall))

fpr, tpr = roc.plot_roc_curve(proba, y_test)
auc = np.trapz(np.flip(tpr), np.flip(fpr))                        # 使用梯形法则计算曲线下面积（注意：沿 x轴的正向进行积分）
print("AUC: {}.".format(auc))
