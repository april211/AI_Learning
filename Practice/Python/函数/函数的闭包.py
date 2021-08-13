# coding=utf-8

def test(name):
    def test_in():      # 函数的嵌套
        print(name)     # 内部函数使用外部函数的变量
        return name     # 内部函数可以有返回值
    return test_in      # 外部函数的返回值为内部函数（也是对象）
# end

func = test("函数的闭包")
print(func())                  # 调用函数并打印返回值（字符串）

# 函数也是对象，也可以当做对象传递
""" 
闭包的概念:
1）存在函数嵌套
2）内部函数可以使用外部函数的变量
3）外部函数的返回值是内部函数
4）内部函数可以存在返回值
"""
