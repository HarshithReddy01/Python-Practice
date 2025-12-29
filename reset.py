pw1 = input("New password: ")
pwd2 = input('Confirm password: ')

if pw1 == pwd2:
    print('Password Changed')
elif pw1.casefold() == pwd2.casefold():
    print('Please check cases')
else:
    print('Passwords not match')
