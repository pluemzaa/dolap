hour_in = int(input())
min_in = int(input())
hour_out = int(input())
min_out = int(input())
in_min = hour_in*60+min_in
out_min = hour_out*60+min_out
total = out_min - in_min
if total <=15:
     pay = 0
     print(“Pay:”+str(pay))
elif total <=180:
     pay = ((total+59)//60)*10
     print(“Pay:”+str(pay))
elif total <=360:
     hour = (total+59)//60
     pay = 3*10+(hour-3)*20
     print(“Pay:”+str(pay))
else:
     pay = 200
     print(“Pay:” + str(pay))