
# random sales dictionary
sales = { 'apple' :  2, 'orange' :  3, 'grapes' :  4 }

items = sales.items()            # 这里返回的不是 List，而是一个 dict_items对象，它不是一个简单的列表，但可以 for遍历
print('Original items:', items)

itemslist = list(sales.items())  # 可以这么写

# delete an item from dictionary
del sales['apple']
print('Updated items:', items)   # 注意：这里打印的是词典的一个对象，是随着词典·动态变化·的

print('Old items:', itemslist)   # 这里的列表则不会变动              



"""
The view object items doesn't itself return a list of sales items but it returns a view of sales's (key, value) pair.

If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.
"""

# https://www.programiz.com/python-programming/methods/dictionary/items
