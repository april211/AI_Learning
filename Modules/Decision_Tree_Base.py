import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from Tree_Node import Node

class DecisionTreeBase:
    def __init__(self, max_depth, get_score, feature_sample_rate=1.0):
        """ 初始化决策树最大深度限制参数、分值函数、特征采样率参数 """
        self.max_depth = max_depth
        self.get_score = get_score
        self.feature_sample_rate = feature_sample_rate
    # end

    def split_data(self, j, theta, X, idx):
        """ 根据选定的特征分割总数据集S(X) idx: range(m)"""
        idx1, idx2 = list(), list()
        for i in idx:
            if(X[i][j] <= theta):            # 特征值小于阈值的，分到 idx1中，对应左子树
                idx1.append(i)
            else:                            # 特征值小于阈值的，分到 idx2中，对应右子树
                idx2.append(i)
        return idx1, idx2
    # end

    def get_random_features(self, n):
        """ 根据特征采样率获得随机挑选的特征编号 n: 总特征数"""
        shuffled = np.random.permutation(n)                 # 获得从 0 ~ n-1 的、经过打乱的随机数组
        size = int(self.feature_sample_rate* n)             # 获取应有特征数
        return shuffled[:size]                              # 截取随机打乱的数组的前 size个数值作为本次选择返回的特征编号
    # end

    def find_best_split(self, X, y, idx):
        """ 找到最好的分割数据成两组的方法（最优化分值函数） """
        m, n = X.shape
        best_score, best_j, best_theta = float("inf"), -1, float("inf")         # 初始化最优记录
        best_idx1, best_idx2 = list(), list()
        selected_j = self.get_random_features(n)
        for j in selected_j:                                                    # 每次循环选定一个随机特征分量
            thetas = set([x[j] for x in X])                                     # 获得与该特征分量有关的所有可能的阈值（与不同的 x[j]数目相等）
            for theta in thetas:                                                # 每次循环选定一个阈值，根据阈值试着切割数据，表现比以前好就记录下来
                idx1, idx2 = self.split_data(j, theta, X, idx)
                if min(len(idx1), len(idx2)) == 0:                              # 这种情况下，有一个数据集数据个数为零（阈值为最小阈值或者最大阈值时）
                    continue                                                    # 选择另一个阈值
                score1, score2 = self.get_score(y, idx1), self.get_score(y, idx2)   # 成功切分数据为两份，首先分别计算左右分值函数值
                w = 1.0* len(idx1) / len(idx)                                       # 公式中两项系数的其中一项（ |Sl| / |S|）
                score = w* score1 + (1-w)* score2                                   # 计算目标函数值
                if score < best_score:                                              # 若当前特征和阈值优于历史最佳，则替换
                    best_score, best_j, best_theta = score, j, theta                # 切分依据（最优目标函数值、特征编号、特征阈值）
                    best_idx1, best_idx2 = idx1, idx2                               # 左右子树根节点数据编号
        return best_j, best_theta, best_idx1, best_idx2, best_score
    # end

    def generate_tree(self, X, y, idx, d):
        """ 构造决策树 idx: range(m) d: 剩余深度（递归） """
        r = Node()                                       # 创立初始结点对象
        r.p = np.average(y[idx], axis=0)                 # 先假设为叶子结点，计算一下预测值，后面可能会中途返回上一层函数
        if d == 0 or len(idx) < 2:                       # 如果设定的深度值为 0，或者数据集中数据个数小于 2（无法再分），是叶子结点，直接返回刚构造的结点
            return r
        current_score = self.get_score(y, idx)           # 计算现在的分值函数值
        j, theta, idx1, idx2, score = self.find_best_split(X, y, idx)       # 尝试划分数据集
        if score >= current_score:                # 划分结果比现在还差，则不再划分，该节点即为叶子结点（例如对分类问题，无法再通过划分数据集来降低熵值）
            return r
        r.j = j                                   # 如果结果更好，决定再次划分数据集，并更新节点划分特征编号和特征阈值
        r.theta = theta
        r.left = self.generate_tree(X, y, idx1, d-1)    # 带着左右划分的数据集，递归地进入下一层的划分
        r.right = self.generate_tree(X, y, idx2, d-1)
        return r
    # end

    def fit(self, X, y):
        """ 训练函数 """
        self.root = self.generate_tree(X, y, range(len(X)), self.max_depth)
    # end

    def get_prediction(self, r, x):
        """ 针对·单个·测试样本进行预测（递归） """
        if r.left is None and r.right is None:
            return r.p
        if x[r.j] <= r.theta:
            return self.get_prediction(r.left, x)
        else:
            return self.get_prediction(r.right, x)
    # end

    def predict(self, X):
        """ 预测函数，给出指定测试数据集的预测结果 """
        y = list()
        for i in range(len(X)):
            y.append(self.get_prediction(self.root, X[i]))
        return np.array(y)
    # end
# end
