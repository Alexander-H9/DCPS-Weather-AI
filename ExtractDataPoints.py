import copy

class Data:
    def __init__(self):
        self.minL = None
        self.minR = None
        self.maxM = None
        self.length = None

    def extract(self, data):

        length = len(data)
        liste = copy.deepcopy(data)
        liste.sort()

        # print("Data: ", data)
        # print("sorted Data: ", liste)
        print("Starting to extract the data")
        print("len of datavector: ", length)
        endFirstThird = length//3
        endSecondThird = int(length//1.5)
        print("endFirstThird: ", endFirstThird, "startSecondThird: ", endSecondThird)

        # get the index of the minimum in the first third
        minPosL = data.index(min(data[0:endFirstThird]))

        # get the index of the minimum in the third third
        minPosR = data.index(min(data[endSecondThird:length]))

        # get the index of the maximum in the middle third
        maxPos = data.index(max(data[endFirstThird:endSecondThird]))
        print("IndexminL: ", minPosL, "IndexminR: ", minPosR, "IndexmaxPos: ", maxPos)

        self.minL = data[minPosL]
        self.minR = data[minPosR]
        self.maxM = data[maxPos]
        self.length = length
        print("minL: ", self.minL, "minR: ", self.minR, "maxM: ", self.maxM, "length: ", self.length)


# d = Data()
# l = [123,5346,1,4,654,24,5346,24,4,66,7,8,6,4,3,45,6,7,3,35,34,2346,67,4,45,25,3,56,3920,2365,34,234,4,324,35,67,89,97,76,324,123,2345,677234,512,5,5,2,4]
# d.extract(l)