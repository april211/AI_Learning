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
X_train, y_train = generate_samples(20)
X_train = poly.fit_transform(X_train)
X_test, y_test = generate_samples(80)
X_test = poly.fit_transform(X_test)

Lambdas, train_r2s, test_r2s = [], [], []

for i in range(0, 200):
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
