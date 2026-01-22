L = [1,2,33,4,2,3,422]
print(len(L))

class duck:
    def talk(self):
        print('Duck is talking')

    def walk(self):
        print('Duck is walking')

class dog:
    def talk(self):
        print('Dog is talking')
    
    def walk(self):
        print('Dog is walking')

def person(pet):
    pet.talk()
    pet.walk()

Duck = duck()
Dog = dog()
person(Duck)
person(Dog)

