d = {1:'One', 10:'Two'}
print(d[10])

for i in d:
    print(i, d[i])

d1 = {1:3.5, 2.5:True, 5+6j:'abc'}
print(d1)

d2 = {1:[12,33], 2:(4,5), 3:{5,4}, 4:{1:1, 2:2}}
print(d2)

#iterable one
s = dict([(1, 'One'), (10, 'Two')])
print(s)

# zip functionn-

l1 = [1,2,3,4]
l2 = ['one', 'two', 'three', 'four', 'five', 'six']
l = dict(zip(l1,l2))
print(l)


# enumerate

s3 = dict(enumerate(l2, start=7))
print(s3)


for x in s3.keys():
    print(x, s3[x])