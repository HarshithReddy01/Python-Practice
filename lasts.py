l =[1,2,3,4,5]
print(l)

L1 = list((3,7,5,9))
print(L1)

L3 = []
print(L3)

x = [2,5,7,4,5,6,6]
x[2] = 15
x.append(25)
x.remove(5)
print(x)


s = [2,5,7,4,5,6,6,9,10]
s1 = print(s[4])
s2 = print(s[ : : -1])

h = [2,5,7,4,5,6,6,9,10]
h[4] = 15
print(h)
h[5] = [10, 'Harshith']
print(h)

h[3:3] = [10]
print(h)
h[9:9] = [10]
print(h)
h.append(10)
print(h)
h[0:0] = [10, 11, 12]
print(h)


k = [1,2,3]
k1 = [8,9,10]
k2 = k+k1
print(k2)
print(k2+[4])


a = [5,6,7,8,9]
for x in a:
    print(x)

b = [5,6,7,8,9]
for i in range(len(b)):
    print(b[i])