from datetime import date

class profile:
    def __init__(self, first, last, year):
        self.__first = first
        self.__last = last
        self.year = year

    @property
    def name(self):
        return f'{self.__first} {self.__last}'
    
    @name.setter
    def name(self, name):
        names = name.strip().split()
        self.__first = names[0]
        self.__last = names[1]

    @property
    def age(self):
        current_year = date.today().year
        return current_year - self.year

if __name__ == "__main__":
    p = profile("Harshith", "Reddy", 2004)

    print("Full Name: ", p.name)
    print("Age: ", p.age)