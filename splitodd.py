nums =[1,2,3,4,4,3,2,5,76,8,6,9]
even_nums = []
odd_nums = []

for i in nums:
    if i % 2 == 0 :
        even_nums.append(i)
    else:
        odd_nums.append(i)
print('Even numbers: ', even_nums)
print('Odd Numbers: ', odd_nums)