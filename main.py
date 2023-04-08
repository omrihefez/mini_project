from generatePoints import generatePointsNoOverlap
from src.lis import LongestIncreasingSubsequenceWeight

A = generatePointsNoOverlap(100, 1000000, 100000)
n = len(A)
  
print("Weight of Longest Increasing Subsequence is ",
       LongestIncreasingSubsequenceWeight(A, n, True))

# constructPrintLIS(A, n)