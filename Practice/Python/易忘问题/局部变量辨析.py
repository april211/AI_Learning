x = 50      # 这里 `x` 并不是全局变量

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)      # 上一行的函数调用并未修改 `x` 的值
