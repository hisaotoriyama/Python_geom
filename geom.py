import math
        
class Shape:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
class Circle(Shape):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r=r
    def round(self) :
        print(self.r * 2 * math.pi)
    def area(self) :
        print(self.r **2 * math.pi)

