from generatePoints import generatePointsNoOverlap
from src.lis import LongestIncreasingSubsequenceWeight, printLIS

A = generatePointsNoOverlap(10000, 1000, 1000)
n = len(A)

weight, LIS = LongestIncreasingSubsequenceWeight(A, n, False)

print("The nodes in the Longest Increasing Subsequence are: ")
printLIS(LIS)
print("Weight of Longest Increasing Subsequence is {}".format(weight))
  
# print("Weight of Longest Increasing Subsequence is ",
#        LongestIncreasingSubsequenceWeight(A, n, True))

# constructPrintLIS(A, n)