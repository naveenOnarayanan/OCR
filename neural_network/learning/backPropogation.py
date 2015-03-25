import random
class BackPropogationLearning:

    def __init__(self, network):
        random.seed(1)
        self.learning_rate = 0.1
        self.E_max = 0.01
        self.E = 0
        self.k = 1
        self.network = network
        

    def train(self, inputs, outputs):
        # TODO
        for i in range(len(inputs)):
            val = self.network.calculate(inputs[i])
            print(val)
    

