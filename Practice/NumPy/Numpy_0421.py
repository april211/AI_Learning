import numpy as np


print("Declare a vector using a list as the argument: ")
v = np.array([1, 2, 3, 4])
print(v)                        # [1 2 3 4]
print(v.shape)                  # (4,)
print()

print("Declare a matrix using a nested list as the argument: ")
M = np.array([[1, 2],
              [3, 4]])
print(M)
print(M.shape)

print("Still the same core type with different shapes: ")
print("Type of v: {}".format(type(v)))
print("Type of M: {}".format(type(M)))
print()

print("M's size: {}".format(M.size))
print()

print("Arguments: start, stop, step: ")
# 如果步长是非整数，最好用 Linspace
# Values are generated within the half-open interval [start, stop) 
# (in other words, the interval including start but excluding stop). 
# For integer arguments the function is equivalent to the Python built-in range function, but returns an ndarray rather than a list.
x = np.arange(0, 10, 1)                    
print(x)

# Returns num evenly spaced samples, calculated over the interval [start, stop].
x = np.linspace(0, 10, 25)                  
print(x)

# Return numbers spaced evenly on a log scale.
# In linear space, the sequence starts at base ** start (base to the power of start) and ends with base ** stop (see endpoint below).
x = np.logspace(start=0, stop=10, num=10, base=np.e)
print(x)

x, y = np.mgrid[0:5, 0:5]
print(x)                        # 每一列都一样，沿着横轴扩展，表示 0轴的度量
print(y)                        # 每一行都一样，沿着纵轴扩展，表示 1轴的度量

r = np.random.rand(5, 5)        # 按照指定的维度和大小，给出一个随机数组，范围：[0, 1)
print(r)

r = np.random.randn(5, 5)       # 按照标准正态分布 (mean=0, variance=1)的概率密度给出指定的维度和大小的随机数组
print(r)

d = np.diag([1, 2, 3])
print(d)

print(M)
print(M.shape)
print(M.itemsize)
print(M.nbytes)
print(M.ndim)

print(v)
print(M)
print(v[0])
print(M[1, 1])          # (axis=0, axis=1) / (纵，横)

print(M[1])             # row 1
M[0, 0] = 7             # assign new value
print(M)

M[0,: ] = 0             # 第 0行的所有列全赋为 0
print(M)

A = np.array([1, 2, 3, 4, 5])
print(A[1:3])           # slicing works just like with lists (the second index is exclusive)

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])    # a quick method of creation of matrix
print(A)
print(A.shape)

row_indices = [1, 2, 3]
print(A[row_indices])               # 取出矩阵的第 1、2、3行

# index masking
B = np.array([n for n in range(5)])
print(B)
row_mask = np.array([True, False, True, False, False])
print(B[row_mask])
print(B[0] is np.ma.masked)
print(B[-1] is np.ma.masked)
print(B)

x = np.ma.array([1, 2, 3], mask=[0, 0, 1])
print(x[0])
print(x[-1])                # masked
print(x[-1] is np.ma.masked)

v1 = np.arange(0, 5)
print(v1)
print(v1 + 2)
print(v1* 2)
print(v1* v1)
print(np.dot(v1, v1))
print(np.dot(A, v1))

# cast changes behavior of + - * etc. to use matrix algebra
print(A)
print(type(A))                  # <class 'numpy.ndarray'>
print(A.dot(A))

M = np.matrix(A)
print(type(M))                  # <class 'numpy.matrix'>
print(M)
print(np.multiply(M, M))        # 对位相乘
print(M.dot(M))                 # 矩阵乘法
print(M * M)                    # 矩阵乘法

# inner product?
print(v)
x1 = v.T* v
print(x1)                       # 星号：对数组执行对应位置相乘，对矩阵执行矩阵乘法运算
print(x1.size)
print(v.T.dot(v))               

C = np.matrix([[1j, 2j], [3j, 4j]])         # complex
print(C)

print(np.conjugate(C))                      # 共轭运算
print(C)
print(C.I)                                  # 求逆运算

print(np.mean(A[:,3]))                      # 求第三列的平均值
print(np.std(A[:,3]), np.var(A[:,3]))       # 标准差、方差
print(A[:,3].min(), A[:,3].max())           # 最大值、最小值

d = np.arange(1, 10)
print(d)
print(sum(d), np.prod(d))

print(np.cumsum(d))                         # 沿着指定轴做累积和
print(np.cumprod(d))                        # 沿着指定轴做累积乘

print(A)
print(np.trace(A))                          # sum of diagonal

m = np.random.rand(3, 3)
print(m)

# use axis parameter to specify how function behaves
print(m.max(), m.max(axis=0))               # 各种最大值

print(A)
# reshape without copying underlying data
n, m = A.shape
B = A.reshape(1, n* m)              # “标签”
print(B)

# modify the array
B[0, 0:5] = 5
print(B)

# ***also changed***
print(A)                        # 注意 A（原矩阵）发生了变化

# creates a copy
B = A.flatten()
B[4] = 7
print(B)                        # 这里的 B是 A一个拷贝，与上面不同，修改 B并不会改变 A  
print(A)

# can insert a dimension in an array
v = np.array([1,2,3])
print(v)
print(v[:, np.newaxis])
print(v[:,np.newaxis].shape, v[np.newaxis,:].shape)     # [axis0, axis1, axis2, ...]

print(np.repeat(v, 5))          # 按照顺序，每个元素重复
print(np.tile(v, 3))            # 堆积原数组，注意与上面的方法区分

w = np.array([5, 6])
print(np.concatenate((v, w), axis=0))

# deep copy
print(A)
B = np.copy(A)
print(B)




# https://blog.csdn.net/zenghaitao0128/article/details/78715140
