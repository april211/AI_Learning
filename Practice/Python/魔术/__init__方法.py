class Person:
    def __init__(self, name):   # 这里的 self 为必须项
        self.name = name
    # 我们不会显式地调用 `__init__` 方法
    
    def say_hi(self):
        print('Hello, my name is {0}.'.format(self.name))
        print('Bye!')

p = Person('Swaroop')
p.say_hi()

# 前面两行同时也能写作
# Person('Swaroop').say_hi()
