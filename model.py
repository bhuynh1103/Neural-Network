class Model:
    def __init__(self, network):
        self.network = network
        self.size = network.sizes
        self.layers = len(network.sizes)
        self.weights = []
        self.biases = []
        for layer in network.layers:
            for neuron in layer.neurons:
                self.weights.append(neuron.weights)
                self.biases.append(neuron.bias)

    def save(self, name):
        with open(name + '.txt', 'w') as f:
            # file = "Name : " + name + "\n"
            # file += "Size : " + str(self.size) + "\n"
            # file += "Number of Layers : " + str(self.layers) + "\n"
            # file += "WEIGHTS : \n"
            # f.write(file)
            # for weightSet in self.weights:
            #     for weight in weightSet:
            #         f.write(str(weight) + "\n")
            #     f.write("\n")
            # f.write("BIASES : \n")
            # for bias in self.biases:
            #     f.write(str(bias) + "\n")
            size = ""
            for layer in self.size:
                size += str(layer)
            f.write(size + "\n")

            for weightSet in self.weights:
                for weight in weightSet:
                    f.write(str(weight) + "\n")
                f.write("\n")
            f.write("\n")
            for bias in self.biases:
                f.write(str(bias) + "\n")
