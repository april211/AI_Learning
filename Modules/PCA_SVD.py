import numpy as np


class PCA_SVD:
    def __init__(self, n_components):
        self.d = n_components
    # end

    def fit_transform(self, X):
        self.mean = X.mean(axis = 0)
        X = X - self.mean
        U, D, VT = np.linalg.svd(X)
        self.W = VT[0:self.d].T
        return X.dot(self.W)
    # end
    
    def inverse_transform(self, Z):
        return Z.dot(self.W.T) + self.mean
    # end
# end
