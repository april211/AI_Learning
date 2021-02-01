import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import Ridge_Regression_Class as rr


def generate_samples(m):
    X = 2* (np.random.rand(m, 1) - 0.5)
    y = X + np.random.normal(0, 0.3, (m, 1))
    return X, y
# end


poly = PolynomialFeatures(degree=10)

np.random.seed(100)
X_train, y_train = generate_samples(30)
X_train = poly.fit_transform(X_train)
X_test, y_test = generate_samples(100)
X_test = poly.fit_transform(X_test)

Lambdas, train_r2s, test_r2s = [], [], []

for i in range(1, 200):
    Lambda = 0.01* i                                            # 每次取不同的 Lambda 值给岭回归模型，让其给出预测
    Lambdas.append(Lambda)                                      # 测试 Lambda 值加入横坐标列表
    ridge = rr.RidgeRegression(Lambda)                          # 建立一个对应 Lambda 参数的岭回归模型雏形
    ridge.fit(X_train, y_train)                                 # 训练该岭回归模型
    y_train_pred = ridge.predict(X_train)                       # 对训练数据做出预测（回归）
    y_test_pred = ridge.predict(X_test)                         # 对测试数据做出预测
    train_r2s.append(ridge.r2_score(y_train, y_train_pred))     # 评价该 Lambda参数下的岭回归模型，加入纵轴列表
    test_r2s.append(ridge.r2_score(y_test, y_test_pred))
# end

# 在两个窗口中分别绘制正则化系数与决定系数 (R2) 的关系图
plt.figure(0)
plt.plot(Lambdas, train_r2s)
plt.figure(1)
plt.plot(Lambdas, test_r2s)

plt.show()



"""
注意：
进行这个代码实验的时候发现：如果原岭回归类（RidgeRegression）中的公式乘以m，
则基本无法实现书上关于在测试数据上，正则化系数增大时，决定系数明显的先增大后减小的关系（原书b图）。
所以在本次提交时，对原岭回归类做了修改，使其与官方代码库中的相应代码的关键位置一致。
"""

"""
单调下降图刻画了正则化系数与决定系数在训练数据上的关系：
随着正则化系数的增大，岭回归的目标函数越来越偏离训练数据的均方误差，因此决定系数越来越小。

“先升后降”图反映了正则化系数与决定系数在测试数据上的关系：
随着正则化系数的增大，模型过度拟合的程度随之降低，导致决定系数在测试数据上的增大；
然而随着正则化系数继续增大，模型又出现了拟合不足的问题，因而决定系数又开始逐渐减小。

在现实应用中，要把握好两者之间的关系，选取最适合模型的正则化系数，
使目标函数中的均方误差部分与正则化部分达到良好的平衡状态。
"""
