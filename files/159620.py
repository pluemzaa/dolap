in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

in_time = in_hour * 60 + in_minute
out_time = out_hour * 60 + out_minute

parked = out_time - in_time

if parked <= 15:
    print("Pay:0")
else:
    hours = (parked + 59) // 60
    if hours <= 3:
        fee = hours * 10
    elif hours <= 6:
        fee = 3 * 10 + (hours - 3) * 20
    else:
        fee = 200
    print("Pay:" + str(fee))