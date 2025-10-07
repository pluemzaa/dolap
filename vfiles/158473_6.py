Inhour = int(input())
Inmin = int(input())
outhour = int(input())
outmin = int(input())

s = Inhour * 60 + Inmin
e = outhour * 60 + outmin
time = e - s

if time <= 15:
    Cost = 0
elif time <= 180:
    if time % 60 != 0:
        hours = time // 60 + 1
    else:
        hours = time // 60
    Cost = hours * 10
elif time <= 360:
    overtime = time - 180
    if overtime % 60 != 0:
        hours = overtime // 60 + 1
    else:
        hours = overtime // 60
    Cost = 30 + hours * 20
else:
    Cost = 200

print("Pay:", Cost)