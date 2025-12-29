import itertools as it

lis = [1,2,3,4,5,2]
perms = it.permutations(lis, r=2)
perm_list = list(perms)
print(perm_list)

for t in perm_list:
    print(t)