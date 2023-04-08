class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lessThan(self, other):
        return self.x < other.x and self.y < other.y

    def greaterThan(self, other):
        return self.x > other.x and self.y > other.y
    
    def greaterOrEqual(self, other):
        return self.x >= other.x and self.y >= other.y