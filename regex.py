import re

print(re.fullmatch('abcharshith', 'abcharshith').group())

print(re.search('very', 'python is very easy').span())


print(re.findall('can', 'can you can a can as a canner'))


ex = '[eimt]{4:}'
print(re.fullmatch(ex, ""))


R = '[A-Z][a-z]+ [A-Z][a-z]+'
print(re.fullmatch(R, 'Harshith Reddy'))


item1 = '[a-zA-Z_][a-zA-Z0-9_]*'
print(re.fullmatch(item1, '_myname'))