import learning.backPropogation
import layer
import neuron

class Network:
    def __init__(self, function, input_count, neuron_count):
        self.input_count = input_count
        self.layer = layer.Layer(function, input_count, neuron_count)

    def calculate(self, inputs):
        self.outputs = self.layer.calculate(inputs)

        return self.outputs