in_hour=int(input(""))
in_minute=int(input(""))
out_hour=int(input(""))
out_minute=int(input(""))
in_total=in_hour*60+in_minute
out_total=out_hour*60+out_minute
parking_minute=out_total-in_total
if parking_minute<=15:
  x=0
elif parking_minute<=180:
  hour=(parking_minute//60)
  x=hour*10
elif parking_minute<=360:
  hour=(parking_minute//60)
  x=hour*20
else:
  x=200
print('Pay:',x,)