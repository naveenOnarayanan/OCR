import learning.backPropogation
import layer
import neuron

class Network:
    def __init__(self, function, input_count, shape):
        self.input_count = input_count
        self.layer_struct = zip(shape[:-1], shape[1:])
        self.layers = []

        for i in range(len(self.layer_struct)):
        	self.layers.append(layer.Layer(function, input_count, self.layer_struct[i]))

   #      for i in range(len(shape)):
			# self.layer[i] = layer.Layer(function, input_count, shape[i])

    def calculate(self, inputs):
    	output = inputs
 
    	for i in range(len(self.layers)):
    		output = self.layers[i].calculate(output) 
    
        return output