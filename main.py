from generatePoints import generatePointsNoOverlap
from src.lis import LongestIncreasingSubsequenceLength

A = generatePointsNoOverlap(100, 1000000, 100000)
n = len(A)
  
print("Length of Longest Increasing Subsequence is ",
       LongestIncreasingSubsequenceLength(A, n, True))

# constructPrintLIS(A, n)