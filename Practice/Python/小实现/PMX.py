###########整数修正############
import random
import copy

# 产生初始种群
a1 = random.sample(range(10), 10)
a2 = random.sample(range(10), 10)
# a1 = [4, 0, 8, 5, 9, 1, 7, 2, 6, 3]
# a2 = [4, 7, 3, 1, 6, 8, 5, 0, 2, 9]

a1_1 = copy.deepcopy(a1)
a2_1 = copy.deepcopy(a2)
print('初始种群为：\n', a1_1, '\n', a2_1)

# 交叉位置
y = random.randint(0,len(a1_1))

# 记录交叉项（后半部分）
fragment1 = a1[y:]
fragment2 = a2[y:]

print('--' * 20, '\n单点交叉交换元素为:\n{}{}\n{}{}'.format(a1_1[:y], fragment1, a2_1[:y], fragment2))
a1_1[y:], a2_1[y:] = a2_1[y:], a1_1[y:]
print('--' * 20, '\n{}位置以后元素实现单点交叉:\n{}{}\n{}{}'.format(y - 1, a1_1[:y], fragment2, a2_1[:y], fragment1))

# 冲突消解
a1_2 = []
a2_2 = []
for i in a1_1[:y]:
    while i in fragment2:
        i = fragment1[fragment2.index(i)]
    a1_2.append(i)
for i in a2_1[:y]:
    while i in fragment1:
        i = fragment2[fragment1.index(i)]
    a2_2.append(i)

child1 = a1_2 + fragment2
child2 = a2_2 + fragment1
print('--' * 20)
print('修正后的子代为:\n{}\n{}'.format(child1, child2))

# 原地址：https://blog.csdn.net/juuunn/article/details/108948237
# 有改动
