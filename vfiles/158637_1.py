FirstHour = int(input())
FirstMin = int(input())
SecondHour = int(input())
SecondMin = int(input())
bgin = FirstHour*60+FirstMin
finl = SecondHour*60+SecondMin
ParkTime = finl-bgin
if ParkTime <= 15:
  pay=0
elif ParkTime <=180 and ParkTime>15 :
  hour=ParkTime//60
if ParkTime%60!=0:
  hour+=1
  pay=hour*10
elif ParkTime<=360:
  hOur=PakTime-180
  hour=hOur//60
if hOur%60!=0:
  hour+=1
  ParkTime=30+hour*20
else :
  pay=200
print("Pay:",Pay)