from node import Node
from lis import LongestIncreasingSubsequenceWeight

A = [ Node(1,1), Node(0,0), Node(1,2), Node (2,2), Node(4,5), Node(5,4) ]

n = len(A)
  
print("Length of Longest Increasing Subsequence is ",
       LongestIncreasingSubsequenceWeight(A, n))