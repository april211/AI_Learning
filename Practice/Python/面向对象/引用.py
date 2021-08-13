# reference 引用

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist 只是指向同一对象的另一种名称
mylist = shoplist

# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象
# 如果前面是：`mylist = list(shoplist)`, 则会产生一个新的对象，他与原对象无关
# 即会输出 `apple`

print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同
# 要记住列表的赋值语句**不会**创建一份副本。你必须使用切片操作来生成一份序列的副本。

""" 你要记住如果你希望创建一份诸如序列等复杂对象的副本（而非整数这种简单的_对象（Object）_），你必须使用切片操作来制作副本。
如果你仅仅是将一个变量名赋予给另一个名称，那么它们都将“查阅”同一个对象，如果你对此不够小心，那么它将造成麻烦。 """

# https://github.com/swaroopch/byte-of-python
