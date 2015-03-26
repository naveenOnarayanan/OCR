import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np

# Square matrix size for pixel values
patternSize = 9

#Make sure inputs and outputs are numpy matrix

#Pass inputs here
input_r = np.array([[-0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5], [-0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, -0.5]])
#Pass outputs here
output_r = np.array([[-0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5], [-0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, -0.5]])

# Network structure, can be changed but I haven't tested with more than 3 layers
shape = (9, 9, 9)

# Initialize network
net = network.Network(functions.SigmoidFunction(1), patternSize, shape)

# Select learning algorithm
learning_alg = learning.BackPropogationLearning(net)

# Start training
learning_alg.train(input_r, output_r)

# Get output
print(learning_alg.run(input_r))