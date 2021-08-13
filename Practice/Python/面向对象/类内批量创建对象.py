class A():
    def __init__(self):
        self.val = 10
 
class B():
    def __init__(self):
        for i in range(10):
            self.__dict__[f'x{i}'] = A()        # 通过循环添加 “名-对象” 键值对


batch = B()
print(batch.__dict__['x1'].val)     # 通过字典访问单个对象的属性
