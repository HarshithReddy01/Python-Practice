import math

class circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return math.pi* self.r * self.r
    
    def perimeter(self):
        return math.pi*2*self.r


c = circle(10)
print(c.perimeter(), c.area())