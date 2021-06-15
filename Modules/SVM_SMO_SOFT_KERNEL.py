from SVM_SMO_SOFT import SoftSVM
from SVM_Kernel import SVM_Kernel


class SoftKernelSVM(SoftSVM, SVM_Kernel):
    """ 软间隔 & 核方法支持向量机 """
    def __init__(self, C=1000, kernel=None) -> None:
        SoftSVM.__init__(self, C=C)
        SVM_Kernel.__init__(self, kernel=kernel)
    # end

    def get_H(self, Lambda, i, j, y):
        return SoftSVM.get_H(self, Lambda, i, j, y)
    # end

    def get_L(self, Lambda, i, j, y):
        return SoftSVM.get_L(self, Lambda, i, j, y)
    # end

    def get_K(self, X_1, X_2):
        return SVM_Kernel.get_K(self, X_1, X_2)
    # end

    def predict(self, X):
        return SVM_Kernel.predict(self, X)
    # end

    def fit(self, X, y, N):
        return SVM_Kernel.fit(self, X, y, N=N)
# end
