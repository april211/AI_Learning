# 测试强制转换

# str 到 List 可以直接转换
text = "zz, p!"
copy = list(text)
print(copy)

# 执行列表操作
a = 'z'
copy.remove(a)

# 列表转字符串
t = ''.join(copy)
print(t)
