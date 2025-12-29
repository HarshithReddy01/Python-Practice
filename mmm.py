import statistics as st

lis = [1,12,3,3,2,4,6,8,4,4,23,67,10]
mean = sum(lis)/len(lis)
print("mean: ", mean)

m = st.median(lis)
print('median: ', m)

mode = st.mode(lis)
print('Mode: ', mode)