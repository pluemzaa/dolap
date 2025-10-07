import math

in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

in_total_minutes = in_hour * 60 + in_minute
out_total_minutes = out_hour * 60 + out_minute

if not (420 <= in_total_minutes < out_total_minutes <= 1380):
    print("Invalid time input.")
else:
    parked_minutes = out_total_minutes - in_total_minutes

    if parked_minutes <= 15:
        pay = 0
    elif parked_minutes <= 180:
        hours = math.ceil(parked_minutes / 60)
        pay = hours * 10
    elif parked_minutes <= 360:
        pay = 3 * 10
        remaining_minutes = parked_minutes - 180
        hours = math.ceil(remaining_minutes / 60)
        pay += hours * 20
    else:
        pay = 200

    print(f"Pay:{pay}")