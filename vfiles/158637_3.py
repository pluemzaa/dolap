Fhour = int(input())
Fminut = int(input())
Sehour = int(input())
Seminut = int(input())

bgin = Fhour * 60 + Fminut
finl = Sehour * 60 + Seminut

parkT = finl - bgin

if parkT <= 15:
    pay = 0
elif parkT <= 180:
    hours = parkT // 60
    if parkT % 60 != 0:
        hours += 1
    pay = hours * 10
elif parkT <= 360:
   parkTT = parkT - 180
    hours = parkTT // 60
    if parkTT % 60 != 0:
        hours += 1
    pay = 30 + hours * 20
else:
    pay = 200

print("Pay:",pay)