in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

in_total = in_hour * 60 + in_minute
out_total = out_hour * 60 + out_minute

total = out_total - in_total

if total <= 15:
    fee = 0
elif total <= 180:
  hours = (total + 59) // 60
  fee = hours * 10
elif total <=360:
  hours = (total + 59) // 60
  fee = 3 * 10 + (hours - 3) * 20
else:
    fee = 200

print("Pay:" + str(fee))