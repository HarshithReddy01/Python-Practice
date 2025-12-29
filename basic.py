a = 201
b = 101_545_458_444
print (a , b)

a= 9.75
b = 15.0
types = type(a)
print(types)
print (a,b)

s1 = bin(10)
s2 = oct(10)
s3 = hex(10)
print(s1, s2, s3)

s1 = bin(True)
print (s1)


f = 16.59
b =True
s1 = "555"
s2 = '0b1010'
s3 = '0xA'

x = int (f) 
x1 = int(b)
x2 = int(s1)
x3 = int(s2, 2)
x4 = int(s3, 16)
print(x, x1, x2, x3, x4)

types = type(x), type(x1), type(x2), type(x3), type(x4)
print(types)


int("125") == 125


length = 15
breadth = 5
area = (length*breadth)
print("Area of the rectangle is:" , area)


x = int(input('Enter your length: '))
y = int(input('Enter your breadth: '))
area = x*y
print('Area of the rectangle is: ', area)