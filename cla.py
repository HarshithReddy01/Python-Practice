class Rectangle:
    def __init__(self):
        self.length = 10
        self.breadth = 5

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    

r = Rectangle()
print("Length is:", r.length) 
print("Breadth is:", r.breadth)
print("Area is:", r.area())
print("Perimeter is:", r.perimeter())


class Rectanglee:
    def __init__(self, l=1, b=1):
        self.lengthh = l
        self.breadthh = b

    def areaa(self):
        return self.lengthh * self.breadthh
    
    def perimetera(self):
        return 2*(self.lengthh+self.breadthh)
    

re = Rectanglee(15,8)
ree = Rectanglee(7, 10)
reee = Rectanglee()
print(re.areaa())
print(reee.perimetera())