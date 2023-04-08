from node import Node

def CeilIndex(A, l, r, key):
  
    while (r - l > 1):
      
        m = l + (r - l)//2
        if (A[m].greaterOrEqual(key)):
            r = m
        else:
            l = m
    return r

def LongestIncreasingSubsequenceLength(A, size):

    #first sort the array by x coordinate
    
    A.sort(key=lambda x: x.x)
  
    # Add boundary case,
    # when array size is one
   
    tailTable = [Node(-1,-1) for i in range(size + 1)]
    len = 0 # always points empty slot
   
    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):
      
        if (A[i].lessThan(tailTable[0])):
  
            # new smallest value
            tailTable[0] = A[i]
   
        elif (A[i].greaterThan(tailTable[len-1])):
  
            # A[i] wants to extend
            # largest subsequence
            tailTable[len] = A[i]
            len+= 1
   
        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tailTable
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i]
          
   
    return len