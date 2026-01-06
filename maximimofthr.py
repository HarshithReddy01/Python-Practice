import re

def max(a,b,c,/):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
maximum = max(5,555,10)
print("The maximum number is: ", maximum)

def si(*,amount,period,year):
    interest = (amount*period*year)/(100)
    return interest
SimpleInterest = si(amount= 50000, year= 2025, period= 60)
print('The Simple Interest is: ', SimpleInterest)

