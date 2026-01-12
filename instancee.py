class Rectanglee:
    count = 0
    def __init__(self, l=1, b=1):
        self.lengthh = l
        self.breadthh = b
        Rectanglee.count += 1

    def areaa(self):
        return self.lengthh * self.breadthh
    
    def perimetera(self):
        return 2*(self.lengthh+self.breadthh)
    
    @classmethod
    def get_count(cls):
        return cls.count

re = Rectanglee(15,8)
ree = Rectanglee(7, 10)
reee = Rectanglee()
print(re.areaa())
print(reee.perimetera())
print(ree.areaa())
print(Rectanglee.get_count())