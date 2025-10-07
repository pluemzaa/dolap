Ahour = int(input())
Amin = int(input())
Bhour = int(input())
Bmin = int(input())
start = Ahour*60+Amin
end = Bhour*60+Bmin
cartime = end-start
if cartime <=15:
  Pay=0
elif cartime <=180:
  time=cartime//60
  if cartime%60 !=0:
  cartime+=1
  Pay=cartime*10
elif cartime <=360:
  max=cartime-180
  cartime=max//60
  if max%60 !=0:
    cartime+=1
   Pay=30+20*cartime
else:
   Pay=200
print("Pay:",Pay)