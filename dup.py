list = [5,5,6,7,8,8,7,1,2,3,4,4,7,8,9,10]
newList = []

for x in list:
    if x not in newList:
        newList.append(x)
print(newList)