from src.lis import LongestIncreasingSubsequenceWeight, printLIS
from random import uniform

def algorithm(nodes, numOfRetries, printProgress = False):
    maxWeight, LIS  = LongestIncreasingSubsequenceWeight(nodes, False)
    while numOfRetries > 0:
        node = flipNode(nodes, LIS)
        if node == None:
            break
        newWeight, newLIS = LongestIncreasingSubsequenceWeight(nodes, False)
        if newWeight <= maxWeight:
            continue
        else:
            node.weight = 1
            numOfRetries -= 1
            if printProgress & (numOfRetries % 10 == 0):
                print("numOfRetries: {}".format(numOfRetries))
    return flippedNodes(nodes)
    


def flipNode(nodes, maxChain):
    while(True):
        i = round(uniform(0, len(nodes) - 1))
        if nodes[i] not in maxChain and nodes[i].weight == 1:
            nodes[i].weight = 2
            return nodes[i]
        else:
            continue
        
def flippedNodes(nodes):
    flipped = []
    for node in nodes:
        if node.weight == 2:
            flipped.append(node)
    return flipped
