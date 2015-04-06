import numpy as np

# This class contains information regarding a network layer and has information regarding
# its neurons with weights and outputs
class Layer:
    def __init__(self, function, input_count, layer_struct):
        self.function = function
        self.input_count = input_count
        self.layer_struct = layer_struct
        # stored as weight(layer1_weights[], ... , layerN_weights[])
        self.weights = []
        self.outputs = []
        self.inputs = []

        (layer1, layer2) = self.layer_struct
        # Initialize a random set of weights for all the neurons in this layer
        self.weights = np.random.normal(scale=0.1, size=(layer2, layer1+1))

        
    # Calculates sig(weights * inputs)
    def calculate(self, inputs):
        # Adding bias node of -1
        inputs = np.append(inputs, -1)
        self.inputs = inputs
        #print("Weight: ", self.weights, "Input: ", inputs)
        
        self.outputs = self.function.eval(self.matrix_dot(self.weights, inputs))
        return self.outputs

    def matrix_dot(self, arr1, arr2):
        #Rotate second arr for matrix multiplication
        return arr1.dot(arr2.T).T
