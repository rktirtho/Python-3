class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def getPoint(self):
        return (self.x, self.y)
    def __str__(self):
        return "Point ({} {})".format(self.x,self.y)
    def __add__(self,another):
        return Point(self.x+another.x,self.y+another.y)

point1 = Point(20,57)
point2 = Point(56,28)
print(point1+point2)
