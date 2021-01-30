import numpy as np


X = np.r_['-1,2,0', np.array([1, 2, 3]), np.array([0, 0, 0]), np.array([4, 5, 6])]               # 使用第一个参数时，注意第二默认参数设置是否合理
print(X)

Y = np.c_['-1,2,0', np.array([1, 2, 3]), np.array([0, 0, 0]), np.array([4, 5, 6])]    # 将切片对象转换为沿第二轴串联的对象
print(Y)

a = np.array([[0, 1, 2], [3, 4, 5]])
b = a + 1
c = np.r_['0,2', a, b]
print(c)

Z = np.r_['1,2,0', [1,2,3], [4,5,6]]
print(Z)


"""
r_、c_字符串参数定义：'起始元素固定位置,最小维数,各数组延伸方向'
此理解方法与官方文档有出入，但目前来讲道理相通，更加简洁。
首先画出坐标轴：逆时针方向，0、1，先将各数组按照第一参数钉在指定的坐标轴上，再按照第三参数沿着指定坐标轴的方向展开。
对于行数大于等于2的矩阵而言，第三参数实测不起作用（针对上例中矩阵c）。
"""

# https://numpy.org/doc/stable/reference/generated/numpy.r_.html
# https://numpy.org/doc/stable/reference/generated/numpy.c_.html
