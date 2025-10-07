hrin = int(input())
minin = int(input())
hrout = int(input())
minout = int(input())
  
invalue = (hrin*60)+minin
outvalue = (hrout*60)+minout
value = outvalue - invalue
  
if value <= 15:
    a = 0
elif 15 < value <= 180:
    a = value//60
    a *= 10
    if 15 < value < 60:
        a += 10
elif 180 < value < 240:
    a = value//60
    a *= 10
    if a % 60 != 0:
        a += 20
elif 240 <= value <= 360:
    a = value//60
    a *= 20
else:
    print("Pay:200")