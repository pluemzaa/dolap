fees = 0

hour_in = int(input())
minutes_in = int(input())
hour_out = int(input())
minutes_out = int(input())

time_in = (hour_in*60+minutes_in)
time_out = (hour_out*60+minutes_out)

total_time = time_out-time_in

if (total_time<=15):
    fees=0
    
if (total_time>15 and total_time<=180):
    main_hour=total_time//60
    sub_hour=total_time%60
    if main_hour < 3 or (main_hour == 3 and sub_hour == 0):
        if sub_hour > 0:
            main_hour+=1
        fees+=10*main_hour
if (total_time>180 and total_time<360):
    main_hour=total_time//60
    sub_hour=total_time%60
    if sub_hour > 0:
        main_hour+=1
    main_hour-=3;fees+=30
    fees+=20*main_hour
if total_time >= 360:
  fees=200

print("Pay:{}".format(str(fees)))