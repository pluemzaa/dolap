Ahour = int(input())
Amin = int(input())
Bhour = int(input())
Bmin = int(input())

start = Ahour * 60 + Amin
end = Bhour * 60 + Bmin
cartime = end - start

if cartime <= 15:
    Pay = 0
elif cartime <= 180:
    if cartime % 60 != 0:
        hours = cartime // 60 + 1
    else:
        hours = cartime // 60
    Pay = hours * 10
elif cartime <= 360:
    overtime = cartime - 180
    if overtime % 60 != 0:
        hours = overtime // 60 + 1
    else:
        hours = overtime // 60
    Pay = 30 + hours * 20
else:
    Pay = 200

print("Pay:", Pay)