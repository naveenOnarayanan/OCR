import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np
import math

class Neural:

    def __init__(self, data):
        self.data = data
        self.learning = []


    def norm_and_flatten(self, mat):
        mat_arr = mat.flatten()
        mat_arr = (mat_arr / 255) - 0.5
        return np.array([mat_arr])



    def train(self):
        desired = []
        inputs = []
        for i in range(len(self.data[0])):
            for j in range(len(self.data)):
                mat = self.data[j][i]
                inputs.append(self.norm_and_flatten(mat))

            #print("Input", inputs, len(inputs))

            patternSize = inputs[0].shape[1]
            desired = np.array([0.9]*patternSize)
            
            net = network.Network(functions.SigmoidFunction(1), patternSize, (patternSize, patternSize, patternSize, 1))
            self.learning.append(learning.BackPropogationLearning(net))
            
            self.learning[-1].train(inputs, desired)
            
            inputs = []
            desired = []
            
            
    def run(self, char):
        outputs = []
        mat = self.norm_and_flatten(char)
        for i in range(len(self.learning)):
            output = self.learning[i].run(mat)
            outputs.append(math.fabs(0.9 - output[0]))
        
        
        minIndex = -1
        minValue = 1
        for i in range(len(outputs)):
            if outputs[i] < minValue:
                minIndex = i
                minValue = outputs[i]
        
        return minIndex