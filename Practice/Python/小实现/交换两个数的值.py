# coding=utf-8

def get_error_details():
    return (2, 'details')
# end

a, b = (3, 7)
print(a, b)

# 实现交换的最快捷方法
a, b = b, a
print(a, b)

# 要注意到 `a, b = <some expression>` 的用法会将表达式的结果解释为具有两个值的一个元组
errnum, errstr = get_error_details()
print(errnum)
print(errstr)
print(errnum, errstr)
