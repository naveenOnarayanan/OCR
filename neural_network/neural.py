import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np

patternSize = 9
patterns = 1

input_r = np.array([[0.3, 0.4]])
output_r = np.array([[0.88]])

net = network.Network(functions.SigmoidFunction(1), patternSize, (2, 2, 1))

learning_alg = learning.BackPropogationLearning(net)

learning_alg.train(input_r, output_r)