import math
import numpy as np
class SigmoidFunction:
    def __init__(self, alpha):
        self.alpha = alpha

    def eval(self, input_val):
        return 1/(1 + np.exp(-self.alpha * input_val))

    def derivative(self, output):
    	return self.alpha * output * (1-output)