import random
class Neuron:
    def __init__(self, function, input_count):
        self.function = function
        self.input_count = input_count;
        self.weights = []

        # +1 for bias weight
        for i in range(self.input_count + 1):
            self.weights.append(random.random())


    # Get output of the neuron of specific inputs
    def calculate(self, inputs):
        sum = 0
        for i in range (len(inputs)):
            sum = sum + self.weights[i] * inputs[i]

        # Bias calculation
        sum = sum + self.weights[-1] * -1

        print(sum)
        self.output = self.function.eval(sum)
        return self.output

