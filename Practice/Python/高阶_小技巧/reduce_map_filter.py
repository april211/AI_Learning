from functools import reduce        # reduce 在 Python 3.x 中需要以此形式导入后，才能使用


a = [1, 2, 3, 4]

# map
b = [i + 4 for i in a]              # 使用列表解析操作列表的每个元素（效率与内置 for相同）
print(b)

b = map(lambda x: x + 4, a)         # 使用 map函数操作列表的每个元素（效率比上面要高，C语言级别）
print(b)                            # 注意：上面的 map 产生了一个对象，需要转换成 list
print(list(b))


# reduce
ans = reduce(lambda x, y: x* y, a)      # 执行递归运算，列表第 1、2个元素先相乘，其结果再与第三个元素相乘）
print(ans)                              

# filter
c = filter(lambda x: x > 0 and x <= 2, a)        # 使用 filter统计列表中符合条件的元素的个数
print(list(c))



# 记住：函数式编程在形式上并不见得比列表解析法简洁，但是效率更高
# lambda map reduce filter
