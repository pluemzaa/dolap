Fhour = int(input())
Fmin = int(input())
Shour = int(input())
Smin = int(input())

begin = Fhour*60 + Fmin
final = Shour*60 + Smin
parktime = final - begin

if parktime <= 15:
   cost = 0
elif parktime <= 180:
   if parktime%60 != 0:
     hours = parktime//60 + 1
   else:
     hours = parktime//60
     cost = hours*10
elif parktime <=360:
    extratime = parktime-180
   if extratime%60 !=0:
     hours = extratime//60+1
   else:
     hours = extratime//60
     cost = 30 + extratime*20
else:
   cost = 200
print("Pay:",cost)