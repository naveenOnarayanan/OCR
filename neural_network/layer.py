import neuron
import numpy as np

class Layer:
    def __init__(self, function, input_count, layer_struct):
        self.function = function
        self.input_count = input_count
        self.layer_struct = layer_struct
        # stored as weight(layer1_weights[], ... , layerN_weights[])
        self.weights = []
        self.outputs = []

        (layer1, layer2) = self.layer_struct
        self.weights = np.random.normal(scale=0.1, size=(layer2, layer1+1))


        print(self.layer_struct)
        print(self.weights)

    def calculate(self, inputs):
        #Adding bias
        inputs = np.append(inputs, -1)
        print("Weight: ", self.weights, "Input: ", inputs)
        
        return self.matrix_dot(self.weights, inputs)

    def matrix_dot(self, arr1, arr2):
        #Rotate second arr for matrix multiplication
        return arr1.dot(arr2.T).T
