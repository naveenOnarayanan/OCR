import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np
import math

class Neural:

    def __init__(self, data):
        self.data = data
        self.bpls = []


    # Converts a 2D array into a 1D array as well as converting the 0 and 255 to 0 and 1
    def norm_and_flatten(self, mat):
        mat_arr = mat.flatten()
        mat_arr = (mat_arr / 255)
        return np.array([mat_arr])

    # Trains the system using the backPropagation learning algorithm
    def train(self):
        test1 = self.data[0][0]
        test2 = self.norm_and_flatten(test1)
        patternSize = test2.shape[1]

        for i in range(len(self.data[0])):
            # Initialize network architecture (1 input layer, 1 hidden layer and 1 output layer)
            neuralNetwork = network.Network(functions.SigmoidFunction(1), patternSize, (patternSize, patternSize, 1))
            bpl = learning.BackPropogationLearning(neuralNetwork)
            inputs = []
            outputs = []
            # Initializes all variances of a specific character for training
            for j in range(len(self.data)):
                for k in range(len(self.data[j])):
                    charMatrix = self.data[j][k]
                    charArray = self.norm_and_flatten(charMatrix)
                    inputs.append(charArray)
                    if k == i:
                        output = [1]
                    else:
                        output = 0
                    outputs.append(output)


            # Tell the multi-network system to train
            bpl.train(inputs, outputs)
            print 'Done Training: ' + str(i)
            self.bpls.append(bpl)


    # Just attempts a feed-forward propagation and gets the max output from all networks
    def run(self, char):
        charArr = self.norm_and_flatten(char)
        maxIndex = None
        maxResult = 0
        for i in range(len(self.bpls)):
            result = self.bpls[i].run(charArr)
            if result > maxResult:
                maxIndex = i
                maxResult = result
        return maxIndex