def fun(*args):
    for x in args:
     if type(x) == int:
        print(x)

v = fun(10,20,30,45,12,45,78, 'Helo')


def funn(a,b,c):
   sum = a+b+c
   prod = a*b*c
   return sum, prod

print(funn(5,6,7))


def result(m1,m2,m3):
   total = m1+m2+m3
   avg = total/3

   if avg >= 45:
      grade = 'Pass'
   else:
      grade = 'Fail'
   return total, avg, grade

print(result(55,100,99))
