import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from Decision_Tree_Base import DecisionTreeBase


def get_var(y, idx):
    """ 方差计算 """
    y_avg = np.average(y[idx])* np.ones(len(idx))
    return (1.0 / len(idx))* np.linalg.norm(y_avg - y[idx], 2)** 2
# end

class DecisionTreeRegressor(DecisionTreeBase):
    """ 决策树回归模型 """
    def __init__(self, max_depth=0, feature_sample_rate=1.0):
        super().__init__(max_depth=max_depth, get_score=get_var, 
                        feature_sample_rate=feature_sample_rate)
    # end
# end
