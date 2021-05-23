import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 指定默认字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 解决保存图像中，负号 '-' 显示为方块的问题
mpl.rcParams['axes.unicode_minus'] = False

plt.figure()    # 启动图像实例

# 设置 X的范围
X = np.linspace(-np.pi, np.pi, 30, endpoint=True)

# 分别计算 cosX和 sinX的值
C, S = np.cos(X), np.sin(X)

# 特殊样式设置
plt.plot(X, C, marker="*", linewidth=3, linestyle="--", color="orange", label='cosine')

# 特殊样式设置
plt.plot(X, S, marker="p", linewidth=3, linestyle="--", color="red", label='sine')

plt.title("正弦与余弦曲线")     # 添加标题
plt.xlabel("-π到π")            # 添加 x标签
plt.ylabel("函数值")           # 添加 y标签
plt.xlim(-5, 5)                # 设置 x轴数值范围
plt.ylim(-1.2, 1.2)            # 设置 y轴数值范围
plt.legend(loc="upper left")   # 启动图例
plt.grid(True)                 # 设置打开网格线

plt.show()                     # 显示图像


# https://blog.csdn.net/qq_27825451/article/details/81630839
