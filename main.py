import pathlib

from src.lis import LongestIncreasingSubsequenceWeight, printLIS
from src.algorithm import algorithm
from src.parse import parse

pwd = pathlib.Path(__file__).parent.resolve().__str__()

for i in range (20, 21):
    numOfFlipped = 0
    for j in range(950, 1001, 10):
        A = parse(pwd + '/data/data{}.csv'.format(i))

        weight, LIS = LongestIncreasingSubsequenceWeight(A, False)

        numOfRetries = j
        flipped = algorithm(A, numOfRetries, True)
        # print("number of nodes flipped: {}".format(len(flipped)))
        # print("The nodes that were flipped are: ")
        # printLIS(flipped)
        if len(flipped) > numOfFlipped:
            numOfFlipped = len(flipped)
            outputFile = open(pwd + '/results/results{}.csv'.format(i), 'w')
            #write flipped to outputFile
            outputFile.write("number of nodes flipped: {}\n".format(len(flipped)))
            for node in flipped:
                outputFile.write("{},{}\n".format(node.x, node.y))
            outputFile.close()
  