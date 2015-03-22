import neuron

class Layer:
    def __init__(self, function, input_count, neuron_count):
        self.function = function
        self.neuron_count = neuron_count
        self.input_count = input_count

        for i in range(neuron_count):
            self.neurons.append(Neuron(function, input_count))
            self.outputs.append(None)

    def compute(inputs):
        for i in range(self.input_count):
            self.outputs[i] = self.neurons[i].calculate(inputs)

        return self.outputs
