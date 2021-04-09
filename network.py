from layer import Layer
from math import exp, log

class Network:
    def __init__(self, sizes):
        self.layers = []
        self.sizes = sizes

        for i in range(len(sizes) - 1):
            self.layers.append(Layer(sizes, i + 1))

    def sigmoid(self, z):
        return 1.0 / (1 + exp(-1 * z))

    def sigmoidPrime(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def transpose(self, matrix):
        r = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(cols):
            nR = []
            for j in range(rows):
                nR.append(0)
            r.append(nR)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                r[i][j] = matrix[j][i]
        return r

    def getWeightsAndBiases(self):
        weights = []
        biases = []
        for layer in self.layers:
            for neuron in layer:
                weights.append(neuron.weights)
                biases.append(neuron.bias)
        return weights, biases

    def outputs(self, input):
        activations = []
        sums = []
        sums.append(input)

        processedInput = [] # input
        # print(processedInput)
        for i in input:
            processedInput.append(self.sigmoid(i))

        activations.append(processedInput)

        prevLayerOutput = self.layers[0].output(processedInput)
        activations.append(prevLayerOutput)

        index = 1
        # print(prevLayerOutput)

        while index < len(self.sizes) - 1:
            prevLayerOutput = self.layers[index].output(prevLayerOutput)
            activations.append(prevLayerOutput)
            sums.append(self.layers[index].getSums(prevLayerOutput))
            # print(prevLayerOutput)
            index += 1

        return prevLayerOutput, activations, sums

    def backprop(self, response, input):
        activation = response[0]
        expected = response[1]
        e = []
        for n in range(10):
            if n == expected:
                e.append(1)
            else:
                e.append(0)

        output = self.outputs(input)

        activations = output[1]
        sums = output[2]

        delta = []
        dW = []
        dB = []

        # l = len(self.layers) - 1
        # for n in range(len(self.layers[l].neurons)):
        #     delta.append(self.sigmoidPrime(sums[l][n]) * 2 * (activations[l][n] - expected))
        # dB.append(delta)
        # w = []
        # for

        delta = []
        l = len(self.layers) - 1
        for n in range(10):
            delta.append(self.sigmoidPrime(sums[l][n]) * 2 * (activations[l][n] - e[n]))
        dB.append(delta)
        nW = []
        for d in range(len(delta)):
            w = []
            for a in range(len(activations[l])):
                w.append(delta[d] * activations[l][a])
            nW.append(w)
        dW.append(nW)
        print(delta)

        for i in range(len(self.layers) - 1):
            # delta = []
            l = len(self.layers) - 2 - i
            # print(len(self.layers[l].neurons))
            sp = []
            for sum in sums[l]:
                sp.append(self.sigmoidPrime(sum))

            newDelta = []
            for n in range(len(self.layers[l].neurons)):
                # print(sums[l][n])
                # print(activations[l][n])
                # print(expected[n])
                '''change this to reflect proper derivative
                delta.append(self.sigmoidPrime(sums[l][n]) * 2 * (activations[l][n] - expected)) # replace expected later
                '''
                weightDeltaDot = 0
                weightSet = self.layers[l].neurons[n].weights
                for w in range(len(weightSet)):
                    print(str(w) + " " + str(n))
                    print(str(weightSet[w]))
                    print(str(delta[n]))
                    print(delta)
                    weightDeltaDot += weightSet[w] * delta[n]
                    # print(weightDeltaDot)
                newDelta.append(weightDeltaDot * sp[n])
            delta = newDelta
            dB.insert(len(dB) - 1, delta)
            nW = []
            for d in range(len(delta)):
                w = []
                for a in range(len(activations[l])):
                    w.append(delta[d] * activations[l][a])
                nW.append(w)
            dW.insert(len(dW) - 1, nW)

            # delta = newDelta
            # dB.insert(len(dB) - 1, delta)
            # nW = []
            # for d in range(len(delta)):
            #     w = []
            #     for a in range(len(activations[l])):
            #         w.append(delta[d] * activations[l][a])
            #     nW.append(w)
            # dW.insert(len(dW) - 1, nW)


        # delta = self.sigmoidPrime(activation) * 2 * (activation - expected)

        return dW, dB

    def cost(self, data):
        activation = data[0]
        expected = data[1]
        sum = 0
        for i in range(activation):
            activation = activation[i]
            if i == expected:
                sum += (activation - 1) ** 2
            else:
                sum += activation ** 2

        return sum

    def loadModel(self, model):
        file = []
        with open(model, "r") as f:
            for line in f:
                if line == "\n":
                    file.append("break")
                else:
                    file.append(float(line[:-1]))
        file[0] = str(int(file[0]))

        sizes = []
        for layer in list(file[0]):
            sizes.append(int(layer))

        weights = []
        weightSet = []
        prev = 0
        index = 0
        for value in file[1:]:
            if value == "break":
                if prev == "break":
                    break
                weights.append(weightSet)
                weightSet = []
            else:
                weightSet.append(value)
            prev = value
            index += 1

        biases = []
        for value in file[index + 2:]:
            biases.append(value)


        self.sizes = sizes
        self.layers = []
        for i in range(len(sizes) - 1):
            self.layers.append(Layer(sizes, i + 1))

        index = 0
        for layer in self.layers:
            for neuron in layer.neurons:
                neuron.weights = weights[index]
                neuron.bias = biases[index]
                index += 1

        # print(weights)
        # print(biases)
        # print(size)
        # print(file)
