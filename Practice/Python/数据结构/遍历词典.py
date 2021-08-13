# 声明两个变量以遍历整个词典
user = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print()

# 按照默认顺序（插入顺序）遍历字典中的所有键
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

for name in favorite_languages.keys():
    print(name.title())
print()

# 结合 if语句使用
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()

# 按照特定的顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")
print()

# 遍历字典中的所有值（为避免重复元素的出现，使用 Set）
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())                         # 这里打印的顺序是不定的
print()


# https://github.com/swaroopch/byte-of-python
