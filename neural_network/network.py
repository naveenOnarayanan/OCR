import learning.backPropogation
import layer

# This class is responsible for a single network and contains information regarding all of
# its layers
class Network:
    def __init__(self, function, input_count, shape):
    	self.function = function
        self.input_count = input_count
        self.layer_struct = zip(shape[:-1], shape[1:])
        self.layer_count = len(self.layer_struct)
        self.layers = []

        # Initialize each of its layers
        for i in range(len(self.layer_struct)):
        	self.layers.append(layer.Layer(function, input_count, self.layer_struct[i]))

    # Runs a calculate on all its layers in this network
    def calculate(self, inputs):
    	output = inputs
 
        # Takes the output of previous layers and propagates them forward to the next layer
    	for i in range(len(self.layers)):
    		output = self.layers[i].calculate(output) 
    
        # Finally returns feed-forward output
        return output