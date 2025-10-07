in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

in_time = in_hour * 60 + in_minute
out_time = out_hour * 60 + out_minute

if out_time < in_time:
    print("Wrong time")
else:
    parked_time = out_time - in_time

    if parked_time <= 15:
        pay = 0
    else:
        hours = (parked_time + 59) // 60
        if hours <= 3:
            pay = hours * 10
        elif hours <= 6:
            pay = 3 * 10 + (hours - 3) * 20
        else:
            pay = 200

    print("Pay:" + str(pay))