import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
import matplotlib.pyplot as plt
import Linear_Regression_Class as lr


def generate_samples(m):
    """用于生成m个服从特征与标签分布的采样"""
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))                # 选择正态分布
    # y = np.zeros(X.shape) + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end

def process_features(X):
    """处理特征（对特征组增补常数：1）"""
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]   # 快速构建数组：This is short-hand for np.r_['-1,2,0', index expression]
    return X
# end


# 产生训练数据和测试数据
np.random.seed(0)                                # 产生固定随机数种子
X_train, y_train = generate_samples(100)
X_train = process_features(X_train)
X_test, y_test = generate_samples(100)           # 按照这种写法，测试点集与训练点集实际上是完全相同的
X_test = process_features(X_test)

# 学习、存储、预测、评估
model = lr.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = model.mean_squared_error(y_test, y_pred)
r2 = model.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))   

# 数据可视化部分
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots(figsize=(9, 4))
ax.scatter(X_train[:,1], y_train, c=list(y_train), cmap=plt.cm.seismic, edgecolors='none', s=2)

# 由模型参数绘制拟合直线（斜截式）
LX = np.linspace(-1.0, 1.0, 100)
LY = model.w[1]* LX + model.w[0]            # y = kx + b
ax.plot(LX, LY, linewidth=1)

plt.show()
