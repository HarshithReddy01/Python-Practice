num = input("Enter the card number: ")
lastDigits = num[15:]
four = 'X' * 4 + ' '
DispNo = four*3 + lastDigits
print(DispNo)