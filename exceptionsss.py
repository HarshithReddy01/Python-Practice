a = 10
b = 0

try:
    c = a//b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")


x = 10
y = 9

if y != 0:
    z = x//y
    print(z)
else:
    print('It should not be zero')

print('End of the code')