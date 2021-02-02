import numpy as np


# 创建行向量法一
a = np.array([1, 2, 3]).reshape((1, -1))
print(a, a.shape)

# 创建行向量法二（推荐写法）
b = np.array([[1, 2, 3]])	         # 注意：这里内层的括号不可以舍弃
print(b, b.shape)

# 创建列向量法一
c = np.array([1, 2, 3]).reshape((-1, 1))
print(c, c.shape)

# 创建列向量法二
d = np.array([[1, 2, 3]]).T
print(d, d.shape)

# 创建列向量法三（注意：这里内层的括号不可以舍弃）
e = np.array([[1]
             ,[2]
             ,[3]])
print(e, e.shape)

# 或者干脆写成：
f = np.array([[1], [2], [3]])
print(e, e.shape)



# https://blog.csdn.net/wintersshi/article/details/80489258
