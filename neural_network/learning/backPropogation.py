import random
class BackPropogationLearning:

    def __init__(self, network):
        random.seed(1)
        self.learning_rate = 0.2
        self.E_max = 0.0001
        self.E = float("inf")
        self.k = 1
        self.network = network


    def train(self, inputs, outputs):
        # TODO
        iterations = 0
        val = 0
        while (self.E > self.E_max):
            self.E = 0
            iterations = iterations + 1
            for i in range(len(inputs)):
                val = self.network.calculate(inputs[i])
                self.E = 0.5*(outputs[i] - val)**2 + self.E
                #print("Error", self.E)
                delta = self.network.function.derivative(val)*(outputs[i] - val)
                self.propogate_error(delta)

        print("Training took " + str(iterations) + " iterations")
        print(val, outputs[0])

        
        
    def run(self, inputs):
        outputs = []
        for i in range(len(inputs)):
            outputs.append(self.network.calculate(inputs[i]))
            
        return outputs

            
    def propogate_error(self, output_delta):
        delta = []
        delta.append(output_delta)
        for i in range(self.network.layer_count -1 , -1, -1):

            # print("Range", i)
            # print("Inputs", self.network.layers[i].inputs)
            # print("Learning Rate", self.learning_rate)
            # print("Delta", delta[-1])


            delta_weights = self.network.layers[i].inputs*self.learning_rate*delta[-1]
            # print("Delta Weights", delta_weights)
            self.network.layers[i].weights = self.network.layers[i].weights + delta_weights

            inputs = self.network.layers[i].inputs
            # print("Inputs", inputs)
            # print("Weights", self.network.layers[i].weights)
            d = self.network.function.derivative(inputs)
            dd = self.network.layers[i].weights * d
            # print("Delta_2", dd*delta[-1])
            delta.append(dd*delta[-1])


            # inputs = self.network.layers[i].inputs
            # if (inputs.shape(1) > delta[-1].shape(1)):
            #     delta[-1]
            # d = self.network.function.derivative() * 
            # delta.append(self.network.function.derivative(self.network.layers[i].inputs))

            # print("Final Weights",self.network.layers[i].weights)

        return
            



