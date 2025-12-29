hours = list(map(int, input("Enter the week hours: ").split(',')))

hourly_rate = 12
total_hours = sum(hours)

if total_hours <= 40 :
    total_pay = total_hours * hourly_rate
else:
    over_pay = total_hours - 40
    total_pay = (40 * hourly_rate) + (over_pay * hourly_rate * 1.5)

print("Total hours:", total_hours)
print("Total pay:", total_pay)