num = int(input("Enter your number: "))
sum = 0
while num > 0 :
    r = num % 10
    sum = sum +r
    num = num//10
print("Sum of the digits is: " , sum)

i = 0
n = 3
while i < 9:
    i = i + 1
    print(n * i)
