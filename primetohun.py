n = 100
for n in range (1,101):
    fact = 0
    for i in range (1, n+1):
        if n % i == 0:
            fact += 1
    if fact == 2:
        print(n)
