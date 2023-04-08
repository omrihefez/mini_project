from src.node import Node
from random import randint

def generatePoints(n, xMax, yMax):
    points = []
    for i in range(n):
        x = randint(0, xMax)
        y = randint(0, yMax)
        points.append(Node(x, y))
    return points

def generatePointsNoOverlap(n, xMax, yMax):
    points = []
    for i in range(n):
        x = randint(0, xMax)
        y = randint(0, yMax)
        while Node(x, y) in points:
            x = randint(0, xMax)
            y = randint(0, yMax)
        points.append(Node(x, y))
    return points