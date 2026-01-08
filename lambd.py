def double(x):
    return x*2

k = lambda x : x*2
print(k(3))

v = lambda g,h : g+h
print(v(5,10))

print((lambda z: z*2)(5000))

L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
f = (filter(lambda p: p%3 == 0, L))
print(list(f))