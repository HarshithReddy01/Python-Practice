s1 = 'Race Car'
s2 = s1.replace(' ', '')
rev = s2[: : -1]
if s2.casefold() == rev.casefold():
    print(s2)
else:
    palindrome = s2.casefold() + rev.casefold()
    print(palindrome)