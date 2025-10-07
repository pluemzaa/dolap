import math

h, m, ho, mo = int(input()), int(input()), int(input()), int(input())

x = (ho * 60 + mo) - (h * 60 + m)

if x <= 15:
    print("pay:0")
elif x <= 180:
    hours = math.ceil(x / 60)
    print("pay:{}".format(hours * 10))
elif x <= 360:
    hours = math.ceil(x / 60)
    if hours <= 3:
        pay = hours * 10
    else:
        pay = 3 * 10 + (hours - 3) * 20
    print("pay:{}".format(pay))
else:
    print("pay:200")