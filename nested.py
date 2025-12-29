import math
amount = int(input('Enter the amount: '))
if amount <= 1000 :
    discount = amount*0.9
    print('The amount after discount is: ', discount)
elif amount > 1000 and amount <= 5000:
    discount = amount*0.85
    print('The amount after discount is: ', discount)
elif amount > 5000 and amount < 10000:
    discount = amount*0.80
    print('The amount after discount is: ', discount)
elif amount >= 10000:
    discount = amount*0.75
    print('The amount after discount is: ', discount)