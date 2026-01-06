original = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3, 'f': 2}
inverted = {}

for i,j in original.items():
    if j not in inverted:
         inverted[j] = {i}
    else:
         inverted[j].add(i)
print("Inverted Dict: ", inverted)
