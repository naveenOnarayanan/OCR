import random

# This calss is responsible for running a back propagation algorithm to help clasify the characters
class BackPropogationLearning:

    def __init__(self, network):
        random.seed(1)
        self.learning_rate = 0.2
        self.E_max = 0.01
        self.E = float("inf")
        self.k = 1
        self.network = network


    # Trains the system
    def train(self, inputs, outputs):
        iterations = 0
        val = 0
        # Keeps running until the error is within the acceptable error mark
        while (self.E > self.E_max):
            self.E = 0
            iterations = iterations + 1
            for i in range(len(inputs)):
                # Calculate the feed-forward propagated output
                val = self.network.calculate(inputs[i])
                # Calculate the global error
                self.E = 0.5*(outputs[i] - val)**2 + self.E
                # Calculate the error signal
                delta = self.network.function.derivative(val)*(outputs[i] - val)
                # Propagate the error to the previous layers
                self.propogate_error(delta)
            print("iteration " + str(iterations) + " error", self.E)

        print("Training took " + str(iterations) + " iterations")
        print(val, outputs[0])


    # Returns a normal feed-forward propagation output
    def run(self, inputs):
        outputs = []
        for i in range(len(inputs)):
            outputs.append(self.network.calculate(inputs[i]))

        return outputs


    # The error is propagated the previous layers and the weights are updated accordingly
    def propogate_error(self, output_delta):
        delta = []
        delta.append(output_delta)
        # Iterate through the layers in reverse order (last layer first)
        for i in range(self.network.layer_count -1 , -1, -1):
            # Calculate new weights based on the error
            delta_weights = self.network.layers[i].inputs*self.learning_rate*delta[-1]
            self.network.layers[i].weights = self.network.layers[i].weights + delta_weights

            # Calculate the next error signal for this layer and propagate it to the previous layers
            inputs = self.network.layers[i].inputs
            d = self.network.function.derivative(inputs)
            dd = self.network.layers[i].weights * d
            delta.append(dd*delta[-1])

        return




