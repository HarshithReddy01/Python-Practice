words = {'Plea', 'Medical', 'leap', 'Decimal', 'pale', 'listen', 'silent', 'enlist'}
result = set()

print('Scrambled word pairs: ')

for x in words:
    for y in words:
        if x != y and sorted(x) == sorted(y):
            pair = tuple(sorted((x, y)))
            result.add(pair)
for pair in result:
    print(pair)


