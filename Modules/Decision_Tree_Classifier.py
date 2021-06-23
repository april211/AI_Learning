import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from Decision_Tree_Base import DecisionTreeBase


def get_entropy(y, idx):
    _, k = y.shape
    p = np.average(y[idx], axis=0)
    return -np.log(p + 0.001* np.random.rand(k)).dot(p.T)               # 技巧：不让 log为无穷大
# end

class DecisionTreeClassifier(DecisionTreeBase):
    """ 决策树分类模型 """
    def __init__(self, max_depth=0, feature_sample_rate=1.0):
        super().__init__(max_depth=max_depth, feature_sample_rate=feature_sample_rate, get_score=get_entropy)
    # end

    def predict_proba(self, X):
        return super().predict(X)
    # end

    def predict(self, X):
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)
    # end
# end
