inhour = int(input())
inmin = int(input())
outhour = int(input())
outmin = int(input())
intime = inhour * 60 + inmin
outtime = outhour * 60 + outmin
parked = outtime - intime
if parked <= 15:
    pay = 0
elif parked <= 180:
    hours = (parked + 59) // 60
    pay = hours * 10
elif parked <= 360:
    hours = (parked + 59) // 60
    pay = 30 + (hours - 3) * 20
else:
    pay = 200
print("Pay:" + str(pay))