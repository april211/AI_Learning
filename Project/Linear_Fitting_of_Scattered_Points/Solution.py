import numpy as np
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



np.random.seed(0)                               # 产生固定随机数种子
X_train, y_train = generate_samples(100)
X_train = process_features(X_train)
X_test, y_test = generate_samples(100)          # 按照这种写法，测试点集与训练点集实际上是完全相同的
X_test = process_features(X_test)

model = lr.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = model.mean_squared_error(y_test, y_pred)
r2 = model.r2_score(y_test, y_pred)
print("mse = {} and r2 = {}.".format(mse, r2))

plt.style.use('seaborn-darkgrid')                       # 在两个坐标系中分别画出训练数据点与测试数据点
fig, ax = plt.subplots(figsize=(9, 4))           # a figure with a 1x2 grid of Axes
ax.scatter(X_train[:,1], y_train, c=list(y_train), cmap=plt.cm.seismic, edgecolors='none', s=2)

LX = np.linspace(-1.0, 1.0, 100)                        # 在两个坐标系中画出模型直线
LY = model.w[1]* LX + model.w[0]
ax.plot(LX, LY, linewidth=1)

plt.show()



"""
column_stack : Stack 1-D arrays as columns into a 2-D array.
r_ : For more detailed documentation.

    Examples
    --------
    >>> np.c_[np.array([1,2,3]), np.array([4,5,6])]
    array([[1, 4],
           [2, 5],
           [3, 6]])
    >>> np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
    array([[1, 2, 3, ..., 4, 5, 6]])
"""
