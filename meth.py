nums = [1,2,3,4,5]
nums.append(15)
nums.extend(range(5,8))
nums.insert(50, 'Harshith Learning Python')
n = nums.copy()
print(nums)
n.append(200)
print(n)