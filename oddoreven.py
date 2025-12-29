num = int(input('Enter your number: '))
if num%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")
age = int(input('Enter your age: '))
if age >= 18 :
    print("You are eligible to vote")
else:
    print('You are not eligible to vote')
age1 = int(input('Enter your age: '))
if age >= 18 and age <=60 :
    print("You are eligible to work")
else:
    print('You are not eligible to work')

marks = int(input('Enter your marks: '))
if marks>=0 and marks<=100 :
    print("Your marks are valid")
else:
    print('Your marks are not valid')
gender = str(input("Enter your gender: "))
if gender == 'Male' or gender == 'male':
    print("you are a man")
else:
    print("you are a women")
letter = str(input("Enter your Letter: "))
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print('Your letter is an vowel')
else:
    print('Your letter is a consonant')

