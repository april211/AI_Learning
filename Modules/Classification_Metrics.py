import numpy as np


def cross_entropy(y_true, y_pred):
    """ 交叉熵函数 """
    return np.average(-y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred))
# end

def accuracy_score(y_true, y_pred):
    """ 准确率计算函数 """
    correct = (y_pred == y_true).astype(np.int)
    return np.average(correct)
# end

def precision_score(y, z):
    """ 精确率计算函数 """
    tp = (z * y).sum()
    fp = (z * (1 - y)).sum()
    if tp + fp == 0:
        return 1.0
    else:
        return tp / (tp + fp)
# end

def recall_score(y, z):
    """ 召回率计算函数 """
    tp = (z * y).sum()
    fn = ((1 - z) * y).sum()
    if tp + fn == 0:
        return 1
    else:
        return tp / (tp + fn)
# end
