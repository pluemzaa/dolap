enter_hour = int(input())
enter_minute = int(input())
exit_hour = int(input())
exit_minute = int(input())
total_enter = (enter_hour*60)+enter_minute
total_exit = (exit_hour*60)+exit_minute
duration_minute = total_exit - total_enter
if duration_minute <= 15:
    pay = 0
elif duration_minute <= 180:
    if duration_minute % 60 == 0:
        duration_hour = duration_minute // 60
    else:
        duration_hour = (duration_minute // 60) + 1
    pay = duration_hour * 10
elif duration_minute <= 360:
    if duration_minute % 60 == 0:
        duration_hour = duration_minute // 60
    else:
        duration_hour = (duration_minute // 60) + 1
    pay = 30 + ((duration_hour- 3) * 20)
else:
    pay = 200
print(f"Pay:{pay}")