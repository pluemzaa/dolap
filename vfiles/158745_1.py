hourin = int(input())
minin = int(input())
hourout = int(input())
minout = int(input())

start = hourin * 60 + minin
end = hourout * 60 + minout
parking = end - start

if parking <= 15:
    cost = 0
elif parking <= 180:
    xh = parking // 60
    if parking % 60 != 0:
        xh += 1
    p = xh * 10
elif parking <= 360:
    extra = parking - 180
    xh = extra // 60
    if extra % 60 != 0:
        xh += 1
    cost = 30 + xh * 20
else:
    cost = 200

print("Pay:",cost)