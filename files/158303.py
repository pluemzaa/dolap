ih = int(input())
im = int(input())
oh = int(input())
om = int(input())

s = ih * 60 + im
e = oh * 60 + om

d = e - s

if d <= 15:
    p = 0
elif d <= 180:
    h = d // 60
    if d % 60 != 0:
        h += 1
    p = h * 10
elif d <= 360:
    extra = d - 180
    h = extra // 60
    if extra % 60 != 0:
        h += 1
    p = 30 + h * 20
else:
    p = 200

print("Pay:",p)