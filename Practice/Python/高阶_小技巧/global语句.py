x = 50      # 对比于前一个例子，这里是全局变量了（下文应用了global语句）
            # 这里的 `x` 必须在程序的顶层

def func(a):    # 这里的参数名不能再是 `x` 了，否则会出现语法错误
    global x        # 应用global语句

    print('x is', x)
    x = 2
    print('Changed global x to', x)


a = 10

func(a)  
print('Value of x is', x)


""" 如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是*全局（Global）*的。我们需要通过 `global` 语句来完成这件事。因为在不使用 `global` 语句的情况下，不可能为一个定义于函数之外的变量赋值。 """

""" `global` 语句用以声明 `x` 是一个全局变量——因此，当我们在函数中为 `x` 进行赋值时，这一改动将影响到我们在主代码块中使用的 `x` 的值。
你可以在同一句 `global` 语句中指定不止一个的全局变量，例如 `global x, y, z`。 """

# https://github.com/swaroopch/byte-of-python
