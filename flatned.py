def flatten(L):
    for i in L:
        if hasattr(i, '__iter__'):
            yield from flatten(i)
        else:
            yield i

f = flatten([1,2,[3,[4,5],6,7],8])
flist = list(f)
print(flist)