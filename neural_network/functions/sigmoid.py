import math
class SigmoidFunction:
    def __init__(self, alpha):
        self.alpha = alpha

    def eval(self, input_val):
        return 1/(1 + math.exp(-self.alpha * input_val))