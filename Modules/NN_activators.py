import numpy as np


class IdentityActivator:
    """ Identity 激活函数 """
    def value(self, s):
        """ 函数值 """
        return s
    # end

    def deriative(self, s):
        """ 一阶导函数值 """
        return 1
    # end
# end

class ReLUActivator:
    """ ReLU 激活函数 """
    def value(self, s):
        """ 函数值 """
        return np.maximum(0, s)
    # end

    def deriative(self, s):
        """ 一阶导函数值 """
        return (s > 0).astype(np.int64)
    # end
# end
