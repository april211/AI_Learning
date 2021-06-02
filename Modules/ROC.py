import numpy as np
import matplotlib.pyplot as plt


def threshold(t, proba):
    """ 阈值分类函数的实现 """
    return (proba >= t).astype(np.int)
# end

def plot_roc_curve(proba, y):
    """ 绘制ROC曲线 """
    iter_cnt = 400
    fpr = np.array([])
    tpr = np.array([]) 
    for i in range(iter_cnt):
        z = threshold((1.0 / iter_cnt)* i, proba)
        tp = (y* z).sum()
        fp = ((1 - y)* z).sum()
        tn = ((1 - y)* (1 - z)).sum()
        fn = (y* (1 - z)).sum()
        fpr = np.append(fpr, 1.0* (fp / (fp + tn)))
        tpr = np.append(tpr, 1.0* (tp / (tp + fn)))
    plt.title("ROC")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.plot(fpr, tpr)
    plt.show()
    return fpr, tpr
