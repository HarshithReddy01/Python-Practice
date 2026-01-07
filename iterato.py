l = "hello there"

for x in l:
    print(x)


Y = [455,4,3222,4,6,4,6,7,9,999,6,5,46,7]
it = iter(Y)
print(next(it))


def myrange(n):
    i = 0
    while i<n:
        yield i
        i += 1

m = myrange(5)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

def days():
    d = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    i = 0
    while True:
        yield d[1]
        i += 1 % 7

h = days() 
print(next(h))