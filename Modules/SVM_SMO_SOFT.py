from SVM_SMO import SVM_SMO


class SoftSVM(SVM_SMO):
    """ 软间隔支持向量机算法实现 """
    def __init__(self, C=1000) -> None:
        super().__init__()
        self.C = C
    # end

    def get_H(self, Lambda, i, j, y):
        C = self.C
        if y[i] == y[j]:
            return min(C, Lambda[i] + Lambda[j])
        else:
            return min(C, C + Lambda[j] - Lambda[i])
    # end

    def get_L(self, Lambda, i, j, y):
        if y[i] == y[j]:
            return max(0, Lambda[i] + Lambda[j] - self.C)
        else:
            return max(0, Lambda[j] - Lambda[i])
    # end
# end
