def fun(n):
    if n > 0 :
        print(n)
        fun(n-1)

v = fun(100)
print(v) 


def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)

factorial = fact(5)
print("The factorial is: ", factorial)