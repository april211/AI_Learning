# 孤星得元组，双星获字典
def total(a = 5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
# end



print(total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1560))
        # total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1560)
        # 不会显示 `None`


""" 要注意到如果 `return` 语句没有搭配任何一个值则代表着 `返回 None`。
    `None` 在 Python 中一个 特殊的类型，代表着虚无。
    举个例子， 它用于指示一个变量没有值，如果有值则它的值便是 `None（虚无）`。
    每一个函数都在其末尾隐含了一句 `return None`，除非你写了你自己的 `return` 语句。"""
