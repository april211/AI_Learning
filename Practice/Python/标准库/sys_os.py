
# 通过 `import` 语句 *导入* `sys` 模块
# `sys` 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的*系统*功能（*sys*tem）。
import sys
import os

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

print("当前目录/程序启动的目录: ")
print(os.getcwd(), end = "\n\n")

""" 如果它不是一个已编译好的模块，即用 Python 编写的模块，
    那么 Python 解释器将从它的 `sys.path` 变量所提供的目录中进行搜索。
    如果找到了对应模块，则该模块中的语句将在开始运行，并*能够*为你所使用。
    在这里需要注意的是，初始化工作只需在我们*第一次*导入模块时完成。 """

# https://github.com/swaroopch/byte-of-python
