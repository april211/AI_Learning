
# class Test
class Test:
    def fun1(self):
        print("Instance method")
    
    @staticmethod
    def fun2():
        print("Static method")
    
    @classmethod
    def fun3(cls):
        print("Class method")
# end

# class Tests inherit from class Test
class Tests(Test):
    @classmethod
    def fun3(cls):
        print("Tests' class method")

print('-----------------------------------')
# 无需实例即可使用类方法和静态方法
Test.fun2()
Test.fun3()

print('-----------------------------------')
# 必须有实例才能用相应的实例方法
a = Test()
a.fun1()
#另一种方式（在继承里经常使用）
Test.fun1(a)

print('-----------------------------------')
# 使用类方法的另一种方式
a.__class__.fun3()

print('-----------------------------------')
# override
Tests.fun3()
print('-----------------------------------')


""" 实例方法，类方法，静态方法都可以通过实例或者类调用，只不过实例方法通过类调用时需要传递实例的引用
三种方法从不同层次上来对方法进行了描述：实例方法针对的是实例，类方法针对的是类，他们都可以继承和重新定义，而静态方法则不能继承，可以认为是全局函数 """

# https://github.com/swaroopch/byte-of-python
