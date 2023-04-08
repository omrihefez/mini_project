class Node:
    def __init__(self, x, y, weight=1):
        self.x = x
        self.y = y
        self.weight = weight

    def lessThan(self, other):
        return self.x < other.x and self.y < other.y

    def greaterThan(self, other):
        return self.x > other.x and self.y > other.y
    
    def greaterOrEqual(self, other):
        return self.x >= other.x and self.y >= other.y