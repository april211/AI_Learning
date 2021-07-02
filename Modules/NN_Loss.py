import numpy as np


class SquaredLoss:
    """ 平方损失函数 """
    def value(self, y, v):
        """ 平方损失函数值 """
        return (v - y)** 2
    # end

    def deriative(self, y, v):
        """ 平方损失一阶导函数值 """
        return 2* (v - y)
    # end
# end

def softmax(v):
    """ softmax函数 """
    e = np.exp(v)
    s = e.sum(axis=0)
    for i in range(len(s)):
        e[i] /= s[i]
    return e
# end

class LogarithmicLoss:
    """ 对数损失函数 """
    def value(self, y, v):
        """ 对数函数值（对v进行softmax处理）"""
        p = softmax(v)
        return -(y* np.log(p)).sum()
    # end

    def deriative(self, y, v):
        """ 对数函数一阶偏导数值（对v进行softmax处理）"""
        p = softmax(v)
        return p - y
    # end
# end
