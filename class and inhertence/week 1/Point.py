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
    def __sub__(self,another):
        return Point(self.x-another.x,self.y-another.y)
    def halfWay(self,target):
        mx=self.x+target.x /2
        my = self.y+target.y / 2
        return Point(mx,my)

point1 = Point(10,30)
point2 = Point(20,40)

mid = point1.halfWay(point2)
print(mid)
