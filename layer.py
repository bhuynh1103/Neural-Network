from neuron import Neuron
from math import exp

class Layer:
    '''
        __init__()
        Creates a layer object which is really just an array of neurons.
        The layers are constructed from an sizes parameter which is an array of
        integers that describes how many nerurons are in each layer of the
        network.
    '''
    def __init__(self, sizes, index):
        self.neurons = []
        self.sizes = sizes
        self.index = index
        # self.isFlat = isFlat
        for i in range(sizes[index]):
            self.neurons.append(Neuron(sizes[index - 1]))
            # if index + 1 != len(sizes):
            #     self.neurons.append(Neuron(sizes[index - 1]))
            # else:
            #     self.neurons.append(Neuron(1))

    def sigmoid(self, z):
        return 1.0 / (1 + exp(-1 * z))

    '''
        output(inputs = array of activations from previous layer)
        outputs an array of normalized activations *sigmoid(z)*
    '''
    def output(self, inputs):
        # r = []
        #
        # # if self.isFlat:
        # #     for input in inputs:
        # #         r.append(self.sigmoid(input))
        # #     return r
        #
        # if self.index + 1 != len(self.sizes):
        #     v = self.sizes[self.index + 1]
        # else:
        #     v = self.sizes[self.index]
        #
        # for i in range(v):
        #     r.append(0)
        # for i in range(len(self.neurons)):
        #     output = self.neurons[i].output(inputs[i])
        #     # print(output)
        #     for i in range(len(r)):
        #         r[i] += output[i]
        #
        # # print(r)
        # for i in range(len(r)):
        #     r[i] = self.sigmoid(r[i])
        # return r

        r = []
        for neuron in self.neurons:
            r.append(self.sigmoid(neuron.output(inputs)))
        return r

    '''
        getSums()
        returns an array of activations that have not been normalized
    '''
    def getSums(self, inputs):
        r = []
        for neuron in self.neurons:
            r.append(neuron.output(inputs))
        return r
