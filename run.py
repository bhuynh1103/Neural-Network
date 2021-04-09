from neuron import Neuron
from layer import Layer
from network import Network
from data import Data
from model import Model

# n = Network([3, 2, 3])

sizes = [784, 16, 16, 10]
input = [1, 2, 3]
input1 = [1, 2]

'''
# n1 = Neuron(3)
# print(n1.output(2))

l1 = Layer(sizes, 0)
l2 = Layer(sizes, 1)
l3 = Layer(sizes, 2)

print(l1.neurons)
print(l2.neurons)
print(l3.neurons)

print(l1.output(input))
print(l2.output(input1))
print(l3.output(input1))
'''

# testNetwork = Network([3, 2, 3])
# print(testNetwork.output([1, 2, 3]))
# testNetwork.loadModel("testmodel.txt")
# print(testNetwork.output([1, 2, 3]))

# m = Model(testNetwork)
# m.save("testmodel")
# testNetwork.loadModel("testmodel.txt")

n1 = Network(sizes)
d = Data()
m = Model(n1)
m.save("testmodel")

sampleData = d.getData(0, 1)[0]

# print(n1.outputs(sampleData[0])[0])
# print(d.toString(0, 10))

# print(n1.backprop(n1.output((sampleData[0]), sampleData[1]), sampleData[] ))
# print(n1.output(sampleData[0])[1][3])
output = n1.outputs(sampleData[0])
# print(str(output[0]) + "\n")
# for layer in output[1]:
#     print(layer)
# print("\n")

# for layer in output[2]:
#     print(layer)


# print(sampleData)



b = n1.backprop(sampleData, d.getData(0, 2)[1][0])
count = 0
for layer in b[0]:
    for neuronW in layer:
        print(str(len(neuronW)) + str(neuronW))
    print(str(count) + "\n")
    count += 1

for layer in b[1]:
    print(str(layer) + "\n")


# print(b[1])

# count = 0
# for layer in n1.layers:
#     for neuron in layer.neurons:
#         print(str(len(neuron.weights)) + str(neuron.weights))
#     print(str(count) + "\n")
#     count += 1


# matrix = [
# [1 , 2 , 3],
# [4 , 5 , 6]
# ]
#
# print(n1.transpose(matrix))
