from src.node import Node
from random import uniform

numberOfDigits = 2

def generatePoints(n, xMax, yMax):
    points = []
    for i in range(n):
        x = round(uniform(0, xMax), numberOfDigits)
        y = round(uniform(0, yMax), numberOfDigits)
        points.append(Node(x, y))
    return points

def generatePointsNoOverlap(n, xMax, yMax):
    points = []
    for i in range(n):
        x = round(uniform(0, xMax), numberOfDigits)
        y = round(uniform(0, yMax), numberOfDigits)
        while Node(x, y) in points:
            x = round(uniform(0, xMax), numberOfDigits)
            y = round(uniform(0, yMax), numberOfDigits)
        points.append(Node(x, y))
    return points