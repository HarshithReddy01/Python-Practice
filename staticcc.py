class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, l):
        if l >= 0:
            self._length = l
        else:
            self._length = 1

    @staticmethod
    def calc_area(length, breadth):
        return length*breadth
    
print(Rectangle.calc_area(10,7))

r = Rectangle(-10,5)
r.length = 100000
print(r.length)