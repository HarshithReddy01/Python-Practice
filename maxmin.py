n = 5
print('Enter' , n , "Numbers : ")
i = 0
Max = float('-inf')
Min = float('inf')
x = 0
while i < n :
    i = i+1
    x = int(input(""))
    if x > Max :
        Max = x
    if x < Min:
        Min = x
print("The min element is : " , Min)
print("The max element is : " , Max)
