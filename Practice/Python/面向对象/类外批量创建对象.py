# coding=utf-8

""" 本质上都是利用字典来实现的 """

class A:
    def __init__(self, val):
        self.val = val
# end

# 循环创建对象
for i in range(10):
    locals()[f'x{i}'] = A(i)        # locals() 函数会以字典类型返回当前位置的全部局部变量

# 使用对象，locals()返回了当前位置的全部局部变量的字典，当然包括上面创建的对象
print(locals()['x1'].val)

# 或者先创建一个空字典：
di = {}

for i in range(10):
    di[f'x{i}'] = A(i)

# 使用对象
print(di['x2'].val)
print(di)
