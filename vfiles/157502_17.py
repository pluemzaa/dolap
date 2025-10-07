hr_in = int(input())
min_in = int(input())
hr_out = int(input())
min_out = int(input())
 
checkin = hr_in*60 + min_in
checkout = hr_out*60 + min_out

total = checkout - checkin


if total >= 360:
    pay = 200
elif total >= 299:
    pay = 90
elif total >= 239:
    pay = 70
elif total >= 181:
    pay = 50
elif total >= 120:
    pay = 30
elif total >= 59:
    pay = 20
elif total > 15:
    pay = 10
else:
    pay = 0

print("Pay:", pay)