#用logistic回归完成乳腺癌预测问题
#计算准确率、精确率、召回率。并画RUC曲线和AUC曲线
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def sigmoid(scores):
    return 1.0/(1.0+np.exp(-scores))

class LogisticRegression:
    def fit(self, X, y, eta_0=10, eta_1=50, N=20000):
        """ 模型训练函数 """
        m, n = X.shape
        cw = np.zeros((n, 1))
        self.w = np.zeros((n, 1))
        for t in range(N):
            i = np.random.randint(m)
            x = X[i].reshape(1, -1)
            pred = sigmoid(x.dot(cw))
            g = x.T* (pred - y[i])
            cw -= (eta_0 / (t + eta_1))* g
            self.w += cw
        self.w /= N

    def predict_proba(self, X):
        """ 完成概率预测任务 """
        return sigmoid(X.dot(self.w))

    def predict(self, X):
        """ 完成类别预测任务 """
        proba = self.predict_proba(X)
        return (proba >= 0.5).astype(np.int)        # 使用了阈值为 0.5的阈值分类函数（或者说最大概率分类函数）

#交叉熵函数
def cross_entropy(y_true,y_pred):
    return np.average(-y_true*np.log(y_pred)-(1-y_true)*np.log(1-y_pred))

#计算准确率
def accuracy_score(y_true,y_pred):
    correct=(y_pred==y_true).astype(np.int)
    return np.average(correct)

#计算精确率
def precision_score(y,z):
    TP=(z*y).sum()
    FP=(z*(1-y)).sum()
    if TP+FP==0:
        return 1.0
    else:
        return TP/(TP+FP)

#计算召回率
def recall_score(y,z):
    TP=(z*y).sum()
    FN=((1-z)*y).sum()
    if TP+FN==0:
        return 1
    else:
        return TP/(TP+FN)

#特征标准化
def process_features(X):
    m,n=X.shape
    scaler=StandardScaler()
    X=scaler.fit_transform(X)
    X=np.c_[np.ones((m,1)),X]
    return X

#绘制ROC曲线
def threshold(t,proba):
    return (proba>=t).astype(np.int)

def plot_roc_curve(proba,y):
    fpr = np.array([])
    tpr = np.array([])
    for i in range(100):
        z=threshold(0.01*i,proba)
        tp=(y*z).sum()
        fp=((1-y)*z).sum()
        tn=((1-y)*(1-z)).sum()
        fn=(y*(1-z)).sum()
        fpr = np.append(fpr, 1.0*fp/(fp+tn))
        tpr = np.append(tpr, 1.0*tp/(tp+fn))
    plt.plot(fpr,tpr)
    plt.show()

#绘制AUC曲线

#导入数据
X,y=load_breast_cancer(return_X_y=True)
y = y.reshape(-1, 1)
#数据分割
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)
X_train=process_features(X_train)
X_test=process_features(X_test)

model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print("accuracy={}".format(accuracy))

precision=precision_score(y_test,y_pred)
print("precision={}".format(precision))

recall=recall_score(y_test,y_pred)
print("recall={}".format(recall))

proba=model.predict_proba(X_test)
print(y_test)
print(proba)
plot_roc_curve(proba,y_test)

'''
    #模型拟合
    def fit(self,X,y,eta_0=10,eta_1=50,N=3000):
        
        m,n=X.shape
        w=np.zeros((n,1)).reshape(-1, 1)
        self.w=np.zeros((n,1)).reshape(-1, 1)
        for t in range(N):
            i=np.random.randint(m)
            x=X[i].reshape(1,-1)
            pred=sigmoid(x.dot(w))
            g=x.T*(pred-y[i])
            w-=(eta_0/(t+eta_1))*g
            self.w+=w
        self.w/=N

#计算概率
    def predict_proba(self,X):
        return sigmoid(X.dot(self.w))

#按照概率分类
    def predict(self,X):
        proba=self.predict_proba(X)
        return (proba>=0.5).astype(np.int)
'''