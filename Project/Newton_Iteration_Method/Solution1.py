""" 寻找一元函数: f(w) = w^3 - w^2 + w + 1 的最小值 ==> 寻找函数 f'(w) 的零点 | f'(w*) == 0 """
""" 这里特意给出了一个无解的例子，你可以自行修改代码进行实验测试 """

def F(w):
    """ 函数: f(w) = w^3 - w^2 + w + 1 """
    return w**3 - w**2 + w + 1
# end

def dF(w):
    """ F(w) 的一阶导函数 """
    return 3* (w**2) - 2* w + 1
# end

def d2F(w):
    """ F(w) 的二阶导函数 """
    return 6* w - 2


epsilon = 1e-4                  # 设定精度
w = 0                           # 初始位置
cnt = 0                         # 记录迭代次数，展示算法收敛的速度
maxw = 1e5                      # *** 迭代次数上限，超过此数终止迭代（防止无解造成无限循环）

while abs(dF(w)) > epsilon and cnt < maxw:
    w -= dF(w) / d2F(w)
    cnt += 1

if cnt < maxw:
    print("We have the solution here: ", end='')
    print("({}, {})".format(w, F(w)))
else:
    print("Maximum number of iterations exceeded!")
