hour = int(input())
    minute = int(input())
    left_hour = int(input())
    left_minute = int(input())

    hour_diff = left_hour - hour
    actual_minute = hour * 60 + minute
    actual_left_minute = left_hour * 60 + left_minute
    time_diff = abs(actual_minute - actual_left_minute)
    hour_count = (time_diff+59)//60


    if hour_count == 0:
        hour_count = 1


    ##First condition
    if time_diff <= 15:
        print('Pay:0')

    ##Second condition
    elif time_diff > 15 and time_diff <= 60*3:
        print('Pay:',hour_count * 10)

    ##Third condition
    elif time_diff > 60*3 and time_diff <= 60*6:
        print('Pay:',hour_count * 20)

    ##Last condition
    else:
        print('Pay:200')

    print(time_diff,hour_count)