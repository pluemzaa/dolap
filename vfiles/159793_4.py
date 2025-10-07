hourin = int(input())
minin = int(input())
hourout = int(input())
minout = int(input())
in_min = (hourin*60)+minin
out_min = (hourout*60)+minout
total = out_min - in_min
if total <= 15:
     pay = 0
     print("Pay:"+str(pay))
elif total <= 180:
     pay = ((total+59)//60)*10
     print("Pay:"+str(pay))
elif total <= 360:
     hour = (total+59)//60
     pay = 3*10+(hour-3)*20
     print("Pay:"+str(pay))
else:
     pay = 200
     print("Pay:"+str(pay))