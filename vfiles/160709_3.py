in_hour = int(input())
in_min = int(input())
out_hour = int(input())
out_min = int(input())

in_total_min = in_hour * 60 + in_min
out_total_min = out_hour * 60 + out_min
total_min = out_total_min - in_total_min

if total_min <= 15:
    pay = 0
elif total_min <= 180:
    hours = (total_min + 59) // 60
    pay = hours * 10
elif total_min <= 360:
    hours = (total_min + 59) // 60
    pay = 30 + (hours - 3) * 20
else:
    pay = 200
print(”Pay:“, pay)