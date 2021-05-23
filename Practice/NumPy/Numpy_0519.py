import numpy as np


print("Export-Numpy与线性代数-1")

print("导入包及查看版本信息")
print(np.__version__)
print()

print("生成对角阵")
x = np.eye(5, dtype=int)
print(x)
print()

print("生成全一矩阵")
x = np.ones((5, 5))
print(x)
print()

print("生成单位方阵")
x = np.identity(3)
print(x)
print()

print("自定义矩阵")
x = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
print()

print("输出矩阵行数和列数")
x = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x.shape)
print()

print("由arange函数构建的矩阵")
ndArray = np.arange(9).reshape(3, 3)
x = np.matrix(ndArray)
print(x)
print()

print("由identity函数构建的全一方阵")
y = np.mat(np.identity(3))
print(y)
print()

print("矩阵相加")
print(x)
print(y)
print(x + y)
print()

print("矩阵相乘")
print(x)
print(x* x)
print()

ndArray = np.arange(9).reshape(3, 3)
b = np.dot(ndArray, ndArray)
print(b)
print()

print("矩阵x的三次方")
print(x)
print(x**3)
print()

print("随机矩阵")
z = np.matrix(np.random.random_integers(1, 50, 9).reshape(3, 3))
print(z)
print()

print("矩阵求逆")
print(z)
print(z.I)
print()

print("矩阵转置")
print(z)
print(z.T)
print()

print("求共轭矩阵")
print(z)
print(z.H)
print()

print("方程组求解")
A = np.mat('3 1 4; 1 5 9; 2 6 5')
b = np.mat([[1], [2], [3]])
x = A.I* b
print(x)
print()

print("返回矩阵A的等价ndarray")
print(A)
print(A.A)
print(type(A.A))
print()

print("返回矩阵A的等价展开ndarray")
print(A)
print(A.A1)
print(type(A.A1))
print()

print("置元素值")
z = np.zeros((2, 3))
print(z)
z[1, 2] = 1
print(z)
print()

print("arange函数，创建一个在给定范围的向量")
z = np.arange(1, 101)
print(z)
print()

print("nonzero函数，寻找非零元素的下标")
nz = np.nonzero([1, 2, 3, 0, 0, 4, 0])
print(nz)
print()

print("diag函数，diagonal对角线")
z = np.diag([1, 2, 3, 4], k = 0)    # 主对角线
print(z)
z = np.diag([1, 2, 3, 4], k = 1)    # 主对角线上一
print(z)
z = np.diag([1, 2, 3, 4], k = -1)   # 主对角线下一
print()

print("random模块的random函数，生成随机数")
Z = np.random.random((3, 3))
print(Z)
print()

print("批量置值")
z=np.zeros((8,8), dtype=int)
z[1::2, ::2] = 1        # ::实为省略了第二个参数
print(z)
"""
上述语句批量的将矩阵中，1、3、5、7行以及0、2、4、6列的元素置为1。
1::2表示行号从1到最后一行，递增行为2，所以确定的行号为：1，3，5，7。
同样::2表示列号从0到最后一列，递增列为2，
所以确定的列号为：0，2，4，6。将这些确定的行列交叉的元素统一置为1。
"""
print()

print("min()、max()函数")
A = np.random.random_integers(1, 50, 9).reshape(3, 3)
print(A)
zmin, zmax = A.min(),A.max()
print(zmin, zmax)
print()


print("函数tile(A,reps),reps即重复的次数，不仅可以是数字，还可以是\
array。tile函数可以简单的理解在地面上铺砖，A就是一块砖，\
tile函数的参数指定将这块砖在行方向上和列方向上各重复几次，\
也就是各铺几个。")
z = np.array([1,2,3,4])
print(z)
z = np.tile(z, 2)         # 默认是列方向上重复两次
print(z)
z = np.tile(z, (1,2))    # 同上
print(z)
z = np.tile(z, (2,1))     # 行方向上重复2次，列方向上重复1次
print(z)
z = np.tile(z, (2,2))     # 行方向上重复2次，列方向上重复2次
print(z)
print()

print("归一化，将矩阵规格化到0～1，即最小的变成0，最大的变成1，\
最小与最大之间的等比缩放。")
A = np.random.random_integers(1, 100, 9).reshape(3, 3)
print(A)
Amax, Amin=A.max(),A.min()
Amax, Amin=A.max(),A.min()
A=(A - Amin) / ( Amax - Amin)
print(A)
print()

print("linspace函数，在给定区间中生成均匀分布的给定个数。")
Z = np.linspace(0, 10, 11, endpoint=True, retstep=False)
print(Z)
print()

print("sort函数。调用random模块中的random函数生成10个随机数，\
然后sort排序。")
Z = np.random.random(10)
Z.sort()
print(Z)
print()

print("allclose函数，判断两个array在误差范围内是否相等")
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.allclose(A, B)
print(equal)
print()

print("mean函数，求平均值")
Z = np.random.random(30)
m = Z.mean()
print(m)
print()

print("sum函数，求和")
A = np.random.randint(1, 10, 9).reshape(3, 3)
print(A)
print(A.sum(axis=0))
print(A.sum(axis=1))    # 注意：0表示列相加，1表示行相加。
print()

print("计算内积")
x = np.array([[1, 2], [3, 4]])
y = np.array([[10, 20], [30, 40]])
print(np.dot(x,y))
print()


print("将数组展开计算内积")
x = np.array([[1, 2], [3, 4]])
y = np.array([[10, 20], [30, 40]])
print(np.vdot(x,y))
print()

print("计算外积")
x = np.array([[1, 2], [3, 4]])
y = np.array([[10, 20], [30, 40]])
print(np.outer(x,y))
print()

print("计算叉积")
a = np.array([1,0,0])
b = np.array([0,1,0])
print(np.cross(a,b))
print()

print("计算行列式")
x = np.array([[4,8],[7,9]])
print(np.linalg.det(x))
print()

print("行列式求逆")
x = np.array([[4,8],[7,9]])
print(np.linalg.inv(x))
print()

print("方程组求解（不可逆时报错）")
print(A)
print(b)
x = np.linalg.solve(A,b)
print(x)
print()

print("特征值分解")
x = np.random.randint(0, 10, 9).reshape(3,3)
print(x)
w, v = np.linalg.eig(x)
print(w)
print(v)
print("其中，w为特征值，v的列向量为特征向量。")
print()


print("复矩阵的分解")
y = np.array([[1, 2j],[-3j, 4]])
w,v=np.linalg.eig(y)
print(w)
print(v)
print()

print("奇异值分解")
print("奇异值分解可以看做特征值分解的扩展，可用于非方阵。")
np.set_printoptions(precision = 4)
A = np.array([3,1,4,1,5,9,2,6,5]).reshape(3,3)
u, sigma, vh = np.linalg.svd(A)
print(u)
print(sigma)
print(vh)
print()

print("QR 分解")
b = np.array([1,2,3]).reshape(3,1)
q, r = np.linalg.qr(A)
x = np.dot(np.linalg.inv(r), np.dot(q.T, b))
print(x)
print()
