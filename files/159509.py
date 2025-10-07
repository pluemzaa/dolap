x = int(input())
y = int(input())
a = int(input())
b = int(input())

intotal = (x*60)+y
outtotal = (a*60)+b

total = outtotal - intotal

if total <=15:
    fee = 0
elif total<=180:
    hours = (total + 59)//60
    fee = hours*10
elif total<=360:
    hours = (total+59)//60
    fee = 3*10+(hours-3)*20
else:
    fee=200
    
print("pay:",srt(fee))