m = 15
for j in range (1, m+1):
    if m % j == 0:
        print(j)


n = 7
fact = 0
for i in range (1, n+1):
    if n % i == 0:
        fact += 1
if fact > 2 :
    print("It is not a prime number")
else:
    print("It is a prime number")