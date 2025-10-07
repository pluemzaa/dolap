hourin = int(input())
minutein = int(input())
hourout = int(input())
minuteuot = int(input())

start = hourin * 60 + minutein
end = hourout * 60 + minuteuot
parking = end - start

if parking <= 15:
    cost = 0
elif parking <= 180:
    hours = parking // 60
    if parking % 60 != 0:
        hours += 1
    cost = hours * 10
elif parking <= 360:
    extra = parking - 180
    hours = extra // 60
    if extra % 60 != 0:
        hours += 1
    cost = 30 + hours * 20
else:
    cost = 200

print("Pay:",cost)