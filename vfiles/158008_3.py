timein_hour = input()
timein_min = input()
timeout_hour = input()
timeout_min = input()

timein_hour = int(timein_hour)
timein_min = int(timein_min)
timeout_hour = int(timeout_hour)
timeout_min = int(timeout_min)

timein_1 = (timein_hour * 60) + timein_min
timeout_1 = (timeout_hour * 60) + timeout_min

total = timeout_1 - timein_1
pay = 0

if (total > 360):
    print("Pay:",pay + 200)
if (total >= 240) and (total <= 360):
    if total % 60 == 0:
        print("Pay:",pay + (total/60) * 20)
    else:
        print("Pay:",pay + ((total//60) * 20) + 20)
if (total > 15) and (total < 240):
    if total % 60 == 0:
        print("Pay:",pay + (total/60) * 10)
    else:
        print("Pay:",pay + ((total//60) * 10) + 10)
if (total <= 15):
    print("Pay:",pay)