import math
enter_hour = int(input())
enter_minute = int(input())
exit_hour = int(input())
exit_minute = int(input())
enter_time_minutes = enter_hour * 60 + enter_minute
exit_time_minutes = exit_hour * 60 + exit_minute
parking_duration_minutes = exit_time_minutes - enter_time_minutes
if parking_duration_minutes <= 15:
    fee = 0
elif parking_duration_minutes <= 180:
    hours = math.ceil(parking_duration_minutes / 60)
    fee = hours * 10
elif parking_duration_minutes <= 360:
    first_3_hours_fee = 3 * 10  
    remaining_minutes = parking_duration_minutes - 180
    remaining_hours = math.ceil(remaining_minutes / 60)
    additional_fee = remaining_hours * 20
    fee = first_3_hours_fee + additional_fee
else:
    fee = 200
print(f”Pay:{fee}“)