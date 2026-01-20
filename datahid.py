class parent:
    def __init__(self,d):
        self._data = d
    
    def show(self):
        print(self._data)

class child(parent):
    def __init__(self,d):
        super().__init__(d)

    def display(self):
        print(self.__data)

p = child(15)
p.show()