import calendar as cal

def next():
    count = 1
    while True:
        h = cal.month_name[count]
        yield h
        count = count % 12 + 1

m = next()

print(m)
