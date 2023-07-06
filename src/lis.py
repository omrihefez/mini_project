from src.node import Node

def CeilIndex(A, l, r, key):
  
    while (r - l > 1):
      
        m = l + (r - l)//2
        if (A[m].greaterOrEqual(key)):
            r = m
        else:
            l = m
    return r

def LongestIncreasingSubsequenceWeight(A, shouldPrintLIS=False):

    #first sort the array by x coordinate
    
    A.sort(key=lambda x: x.x)

    LIS = longest_increasing_weighted_sequence(A)
    weight = 0
    for e in LIS:
        weight += e.weight
    if shouldPrintLIS:
        printLIS(LIS)
    return weight, LIS



# Utility function to print LIS
def printLIS(arr: list):
    for e in arr:
        print("Node({},{}) with weight {}".format(e.x,e.y, e.weight), end="\n")
    print()
 
# Function to construct and print Longest Increasing
# Subsequence
def constructPrintLIS(arr: list, n: int):

    arr.sort(key=lambda x: x.x)

    # L[i] - The longest increasing sub-sequence
    # ends with arr[i]
    l = [[] for i in range(n)]
 
    # L[0] is equal to arr[0]
    l[0].append(arr[0])
 
    # start from index 1
    for i in range(1, n):
 
        # do for every j less than i
        for j in range(i):
 
            # L[i] = {Max(L[j])} + arr[i]
            # where j < i and arr[j] < arr[i]
            if arr[i].greaterThan(arr[j]) and (len(l[i]) < len(l[j]) + 1):
                l[i] = l[j].copy()
 
        # L[i] ends with arr[i]
        l[i].append(arr[i])
 
    # L[i] now stores increasing sub-sequence of
    # arr[0..i] that ends with arr[i]
    maxx = l[0]
 
    # LIS will be max of all increasing sub-
    # sequences of arr
    for x in l:
        if len(x) > len(maxx):
            maxx = x
 
    # max will contain LIS
    return maxx


def longest_increasing_weighted_sequence(nodes):
    n = len(nodes)
    # Sort the nodes in increasing order of x and y
    nodes.sort(key=lambda node: (node.x, node.y))
    # Initialize the memoization table
    memo = [0] * n
    # Initialize the longest increasing weighted sequence to be the weight of each node
    prev = [-1] * n
    for i in range(n):
        memo[i] = nodes[i].weight
        prev[i] = -1
    # Dynamic programming: find the longest increasing weighted sequence that ends at each node
    for i in range(1, n):
        for j in range(i):
            if nodes[i].greaterOrEqual(nodes[j]) and memo[i] < memo[j] + nodes[i].weight:
                memo[i] = memo[j] + nodes[i].weight
                prev[i] = j
    # Find the index of the node with the maximum weight
    max_index = 0
    for i in range(1, n):
        if memo[i] > memo[max_index]:
            max_index = i
    # Reconstruct the longest increasing weighted sequence
    sequence = []
    while max_index != -1:
        sequence.append(nodes[max_index])
        max_index = prev[max_index]
    # Reverse the sequence to get it in the correct order
    sequence.reverse()
    # Return the list of nodes in the longest increasing weighted sequence
    return sequence