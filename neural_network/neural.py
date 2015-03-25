import network
import learning.backPropogation as learning
import functions.sigmoid as functions

patternSize = 9
patterns = 1

input_r = [[0, 1, 0, 0, 1, 0, 0, 1, 0]]
output_r = [[0, 1, 0, 0, 1, 0, 0, 1, 0]]

net = network.Network(functions.SigmoidFunction(1), patternSize, patterns)

learning_alg = learning.BackPropogationLearning(net)

learning_alg.train(input_r, output_r)