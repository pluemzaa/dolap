come_hour = int(input())
come_min = int(input())
out_hour = int(input())
out_min = int(input())

come_total_min = come_hour * 60 + come_min
out_total_min = out_hour * 60 + out_min
total_min = out_total_min - come_total_min

if total_min <= 15:
    pay = 0
elif total_min <= 180:  # 3 ชม.
    hours = (total_min + 59) // 60
    pay = hours * 10
elif total_min <= 360:  # 6 ชม.
    hours = (total_min + 59) // 60
    pay = 30 + (hours - 3) * 20
else:
    pay = 200
print(”Pay:“, pay)