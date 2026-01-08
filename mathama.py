v = abs(-1000)
print(v) 

print(round(5.6))

print(print.__dir__)

def outer():
    def inner():
        print('Inner')
    print('Outer')
    inner()

print(outer())