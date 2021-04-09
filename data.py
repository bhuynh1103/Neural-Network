import gzip

class Data:
    # def __init__(self):
    #     self.trainingData = []
    #     with gzip.open('train-images-idx3-ubyte.gz', 'rb') as f:
    #         # print(f.read()[:16])
    #         for byte in f.read()[0 : 16]:
    #             self.trainingData.append(hex(byte))

    # returns data as list of '[image, label]' items
    def getData(self, i, j):
        bytes = []
        with gzip.open('train-images-idx3-ubyte.gz', 'rb') as f:
            for byte in f.read()[16 + 784 * i : 16 + 784 * (j + 1)]:
                bytes.append(byte)

        images = []
        image = []
        pix = 0
        for byte in bytes:
            image.append(byte)
            pix += 1
            if pix == 784:
                images.append(image)
                image = []
                pix = 0

        labels = []
        with gzip.open('train-labels-idx1-ubyte.gz', 'rb') as f:
            for byte in f.read()[8 + i : 8 + j + 1]:
                labels.append(byte)

        r = []
        for i, l in zip(images, labels):
            r.append((i, l))

        return r

    # returns string representation of an image array
    def imageToString(self, image):
        col = 0
        str = ""
        for pix in image:
            if pix > 200:
                str += "@"
            elif pix > 150:
                str += "0"
            elif pix > 100:
                str += "O"
            else:
                str += "."

            col += 1
            if col == 28:
                col = 0
                str += "\n"

        return str

    # returns string representation of data
    def toString(self, i, j):
        r = ""
        for pair in self.getData(i, j):
            r += self.imageToString(pair[0]) + str(pair[1]) + "\n\n"

        return r
