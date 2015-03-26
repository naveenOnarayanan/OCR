import network
import learning.backPropogation as learning
import functions.sigmoid as functions
import numpy as np

class Neural:

	def __init__(self, data):
		self.data = data
		self.learning = []


	def norm_and_flatten(self, mat):
		mat_arr = mat.flatten()
		mat_arr = (mat_arr / 255) - 0.5
		return mat_arr



	def train(self):
		desired = np.array([0.95])
		inputs = np.array([])
		for i in range(data.shape[1]):
			for j in range(data.shape[0]):
				mat = data[j][i]
				inputs = np.append(inputs, mat)

			print("Input", inputs)

			patternSize = inputs.shape[1]
			net = network.Network(functions.SigmoidFunction(1), patternSize, (patternSize, patternSize, 1))
			self.learning.append(learning.BackPropogationLearning(net))

			self.learning[-1].train(inputs, desired)
