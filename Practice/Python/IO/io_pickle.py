# 本文件名不能是 `pickle`，会导致脚本文件名称与标准库pickle命名冲突
import pickle

# 我们存储相关对象的文件的名称
shoplistfile = "shoplist.data"

# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件 (Write Binary mode)
f = open(shoplistfile, 'wb')

# 转储对象至文件（封装）
pickle.dump(shoplist, f)

# 关闭文件
f.close()

# 清除 shoplist 变量（必须要有）
del shoplist

# 重新打开存储文件 (Read Binary mode)
f = open(shoplistfile, 'rb')

# 从文件中载入对象（拆封）
storedlist = pickle.load(f)
print(storedlist)

""" Python 提供了一个叫作 `Pickle` 的标准模块，通过它你可以将_任何_纯 Python 对象存储到一个文件中，并在稍后将其取回。
这叫作*持久地（Persistently）*存储对象。 """

# https://github.com/swaroopch/byte-of-python
