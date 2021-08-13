# “ab”是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}


print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

# 获取字典列表，并删除最后一个元素
book = list(ab.items())
print(book, end = "\n\n")
book.pop()

for name, address in book:
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

# 我们可以利用 `in` 运算符来检查某对 键值—值 配对是否存在。
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# https://github.com/swaroopch/byte-of-python
