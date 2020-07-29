class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def getPoint(self):
        return (self.x, self.y)

point1 = Point(20,57)
point2 = Point(56,28)
print(point1.getPoint())
