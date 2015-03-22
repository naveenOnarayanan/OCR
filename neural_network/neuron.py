class Neuron:
    def __init__(self, function, input_count):
        self.function = function
        self.input_count = input_count

        

    # Get output of the neuron of specific inputs
    def calculate(inputs):
        sum = 0
        for i in range (len(inputs)):
            sum = sum + weights[i] * input[i]

        self.output = function.eval(sum)
        return self.output

