# format
# -------------------------------------------------
print('-------------------------------------------')

# 定义
age = 20
name = 'Swaroop'
book = 'A Byte of Python'

# 转换至字符串的工作将由 `format` 方法自动完成，而不是需要明确转换至字符串
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# -------------------------------------------------
print('-------------------------------------------')

# 去掉括号内的数字也可以
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# -------------------------------------------------
print('-------------------------------------------')

# 还可以这样，基于关键词输出
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# 不可.format(name, book), 必须使用参数表名

# -------------------------------------------------
print('-------------------------------------------')

# 精准的格式控制

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0 / 3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))

# 尝试控制整数宽度为7，并填充0
print('{0:07d}'.format(3))
print("{0:07d}".format(9))

# 合并使用（小数点也算1个宽度）
print('{0:08.3f}'.format(1.0 / 3))

# -------------------------------------------------
print('-------------------------------------------')

# print默认以 '\n' 结尾。要指定结尾符，应当这样做：
print('a', end='')       # 句末不换行的写法。即指定结尾符为''
print('b', end='')
print()  # 这里有默认换行

print('a', end=' ')      # 或者你可以指定以一个空格结尾
print('b', end=' ')
print('c')               # 这里有默认换行

# -------------------------------------------------
print('-------------------------------------------')
