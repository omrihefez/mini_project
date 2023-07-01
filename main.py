from generatePoints import generatePointsNoOverlap
from src.lis import LongestIncreasingSubsequenceWeight, printLIS
from src.algorithm import algorithm
from src.parse import parse

for i in range (1, 21):
    numOfFlipped = 0
    for j in range(1, 1001, 10):
        A = parse('/home/omri/study/mini_project/data/data{}.csv'.format(i))

        weight, LIS = LongestIncreasingSubsequenceWeight(A, False)

        # print("The nodes in the Longest Increasing Subsequence are: ")
        # printLIS(LIS)
        # print("Weight of Longest Increasing Subsequence is {}".format(weight))

        numOfRetries = j
        flipped = algorithm(A, numOfRetries)
        # print("number of nodes flipped: {}".format(len(flipped)))
        # print("The nodes that were flipped are: ")
        # printLIS(flipped)
        if len(flipped) > numOfFlipped:
            numOfFlipped = len(flipped)
            outputFile = open('/home/omri/study/mini_project/results/results{}.csv'.format(i), 'w')
            #write flipped to outputFile
            outputFile.write("number of nodes flipped: {}\n".format(len(flipped)))
            for node in flipped:
                outputFile.write("node - {},{}, weight - {}\n".format(node.x, node.y, node.weight))
            outputFile.close()
  
# print("Weight of Longest Increasing Subsequence is ",
#        LongestIncreasingSubsequenceWeight(A, n, True))

# constructPrintLIS(A, n)