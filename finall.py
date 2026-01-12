class ageError(Exception):
    pass

def valid(age):
    if age > 18 and age <= 60:
        return True
    else:
        raise ageError('Age should be between 18-60, You cannot work come after you rurn 18 kiddo')
    
name = input('Enter Name: ')
age = int(input('Enter Age: '))

try:
    valid(age)
    print('You can work')
except ageError as e:
    print(e)