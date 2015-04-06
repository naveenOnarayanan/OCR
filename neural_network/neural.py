import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np
import math

class Neural:

    def __init__(self, data):
        self.data = data
        self.bpls = []


    def norm_and_flatten(self, mat):
        mat_arr = mat.flatten()
        mat_arr = (mat_arr / 255)
        return np.array([mat_arr])

    def train(self):
        test1 = self.data[0][0]
        test2 = self.norm_and_flatten(test1)
        patternSize = test2.shape[1]

        for i in range(len(self.data[0])):
            neuralNetwork = network.Network(functions.SigmoidFunction(1), patternSize, (patternSize, patternSize, 1))
            bpl = learning.BackPropogationLearning(neuralNetwork)
            inputs = []
            outputs = []
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

            bpl.train(inputs, outputs)
            print 'Done Training: ' + str(i)
            self.bpls.append(bpl)


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