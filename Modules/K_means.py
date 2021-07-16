import numpy as np


class K_Means:
    """ K均值算法 """
    def __init__(self, n_clusters = 1, max_iter = 50, random_state=0):
        self.k = n_clusters
        self.max_iter = max_iter
        np.random.seed(random_state)
    # end

    def assign_to_centers(self, centers, X):
        """ 将样本点分配到现有的各中心 """
        assignments = []
        for i in range(len(X)):
            distances = [np.linalg.norm(X[i] - centers[j], 2) for j in range(self.k)] 
            assignments.append(np.argmin(distances))
        return assignments 
    # end

    def adjust_centers(self, assignments, X):
        """ 根据聚类结果调整中心 """
        new_centers = []
        for j in range(self.k):
            cluster_j = [X[i] for i in range(len(X)) if assignments[i] == j]            # 取点
            new_centers.append(np.mean(cluster_j, axis=0))                              # 求该类各个样本点的均值
        return new_centers  
    # end

    def fit_transform(self, X):
        """ 返回各个中心的位置和各个样本点的类别归属情况 """
        idx = np.random.randint(0, len(X), self.k)                      # 在 [0, len(X)) 范围内随机取出 k个数
        centers = [X[i] for i in idx]                                   # 取出初始样本点
        for iter in range(self.max_iter):
            assignments = self.assign_to_centers(centers, X)
            centers = self.adjust_centers(assignments, X)
        return np.array(centers), np.array(assignments)
    # end
# end
