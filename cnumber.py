n = int(input('Enter your number: '))
i = 0
while n>0:
    i = i+1
    n = n//10
print('Number of digits are : ' , i)