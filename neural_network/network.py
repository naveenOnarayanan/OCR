import learning.backPropogation
import neuron

class Network:
    def __init__(self, function, input_count, neuron_count):
        self.input_count = input_count
        self.output_count = output_count
        self.layer = Layer(function, input_count, neuron_count)

    def calculate(inputs):
        self.outputs = self.layer.calculate(inputs)

        return self.outputs