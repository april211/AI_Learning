import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from Decision_Tree_Classifier import DecisionTreeClassifier


class RandomForestClassifier:
    """ 随机森林分类器（集成学习思想） """
    def __init__(self, num_trees, max_depth, feature_sample_rate, 
                data_sample_rate, random_state=0):
        """ 初始化随机森林树的数目、树的深度、特征采样率、训练数据采样率 """
        self.max_depth, self.num_trees = max_depth, num_trees
        self.feature_sample_rate = feature_sample_rate
        self.data_sample_rate = data_sample_rate
        self.trees = []
        np.random.seed(random_state)
    # end

    def get_data_samples(self, X, y):
        """ 按照比例，随机选取一部分训练数据 """
        shuffled_indices = np.random.permutation(len(X))
        size = int(self.data_sample_rate* len(X))
        selected_indices = shuffled_indices[:size]
        return X[selected_indices], y[selected_indices]
    # end

    def fit(self, X, y):
        """ 训练函数 """
        for i in range(self.num_trees):
            X_t, y_t = self.get_data_samples(X, y)
            model = DecisionTreeClassifier(max_depth=self.max_depth,                            # 训练多个决策树作为弱模型
                                          feature_sample_rate=self.feature_sample_rate)
            print(i)
            model.fit(X_t, y_t)
            self.trees.append(model)
    # end

    def predict(self, X):
        """ 预测函数 """
        y = []
        for i in range(len(X)):
            preds = [np.asscalar(tree.predict(X[i].reshape(1, -1))) for tree in self.trees]
            y.append(max(set(preds), key=preds.count))              # 参照众数得出结果
        return np.array(y)
    # end
# end
