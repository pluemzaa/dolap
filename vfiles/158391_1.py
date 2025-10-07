in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

in_total = in_hour * 60 + in_minute
out_total = out_hour * 60 + out_minute

duration = out_total - in_total

if duration <= 15:
    pay = 0
elif duration <= 180:
    hours = (duration + 59) // 60
    pay = hours * 10
elif duration <= 360:
    hours = (duration + 59) // 60
    pay = 30 + (hours - 3) * 20
else:
    pay = 200

print(f"Pay:{pay}")