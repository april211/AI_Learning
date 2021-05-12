import sys, os
sys.path.append(os.getcwd() + r'\Modules')
import numpy as np
import matplotlib.pyplot as plt
import Hubber_SubGD as hs
import Linear_Regression_Class as lr
from sklearn.preprocessing import StandardScaler

def generate_samples(m, k):
    """ 产生含有k个异常数据、m个正常线性数据的数据集 """
    X_normal = 2* (np.random.rand(m, 1) - 0.5)
    y_normal = X_normal + np.random.normal(0, 0.1, (m, 1))
    X_outlier = 2* (np.random.rand(k, 1) - 0.5)
    y_outlier = X_outlier + np.random.normal(3, 0.1, (k, 1))
    X = np.concatenate((X_normal, X_outlier), axis=0)
    y = np.concatenate((y_normal, y_outlier), axis=0)
    return X, y
# end

def process_features(X):
    """ 加全1列 """
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]                   # 注意：这一步必须在标准化之后实施
    return X
# end

np.random.seed(0)
normal_spn = 100                    # 正常数据数量
outlin_spn = 10                     # 异常数据数量
X, y = generate_samples(normal_spn, outlin_spn)
X = X.reshape(normal_spn + outlin_spn, -1)
y = y.reshape(normal_spn + outlin_spn, -1)

X_proc = process_features(X)

# print(X.shape, y.shape, X_proc.shape)
model_l = lr.LinearRegression()         # 使用普通线性回归模型作为对照
model_l.fit(X_proc, y)

model_h = hs.Hubber_SubGD(epsilon=0.2)
model_h.fit(X_proc, y, eta=0.01, N=4000)

fig, ax = plt.subplots(1, 1, figsize=(5, 4))
ax.scatter(X, y, s=5, c='b')
LX = np.linspace(-1, 1, 500).reshape(500, 1)

LX_proc = process_features(LX)
pred_l = model_l.predict(LX_proc)
pred_h = model_h.predict(LX_proc)

ax.plot(LX, pred_l, label="LinearRegression model", color='red')
ax.plot(LX, pred_h, label="Hubber_SubGD model", color='green')
ax.legend()

plt.show()
