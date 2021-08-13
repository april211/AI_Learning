#coding=utf-8
""" 利用字典自带方法：fromkeys(seq, value) 来批量创建·键·值 """

seq = ['p1', 'p2', 'p3', 'p4']            # List

dict0 = {}                          # Dict

dict0 = dict0.fromkeys(seq)         # 缺省第二参数（值）
print(str(dict0))

dict1 = {}                          # Dict
dict1 = dict1.fromkeys(seq, 14)     # 完整
print(str(dict1))

# https://github.com/swaroopch/byte-of-python
