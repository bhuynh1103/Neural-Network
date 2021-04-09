from random import gauss
from math import exp

class Neuron:
    '''
        __init__()
        Creates neuron based on how many input activations the
        neuron receives and creates random initialization of weights
        and biases accordingly
    '''
    def __init__(self, inputs):
        self.weights = []
        self.bias = gauss(0, 1)
        self.inputs = inputs

        for i in range(inputs):
            self.weights.append(gauss(0, 1))

            # self.weights.append(i + 1)
    '''
        sigmoid(z = weighted sum that needs normalization)
        Sigmoid function which takes a number from -inf to inf and
        constrains the value to between -1 and 1
    '''
    def sigmoid(self, z):
        return 1.0 / (1 + exp(-1 * z))

    '''
        outputs(inputs = array of activations from previous layer)
        outputs a single weighted sum (not normalized under sigmoid yet)
        according to the input activations received by the neuron
    '''
    def output(self, inputs):
        # r = []
        # for i in range(self.outputs):
        #     r.append(input * self.weights[i] + self.bias)
        # return r

        r = 0
        for i in range(len(inputs)):
            r += inputs[i] * self.weights[i]
        r += self.bias
        return r
