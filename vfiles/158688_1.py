hinc = int(input())
minc = int(input())
hout = int(input())
mout = int(input())
i = hinc * 60 + minc
out = hout * 60 + mout
time = i - out
if time <= 0 and i < 420 and out > 1380:
    print("หยุดให้บริการ")
elif time <= 15:
    print("จ่าย:0")
elif time > 15 and time <= 180:
    ค่าจอด  = time // 60 * 10
    print("pay",ค่าจอด)   
elif time > 180 and time <= 360:
    ค่าจอด  = time // 60 * 20
    print("pay",ค่าจอด)
else:
    print("Pay:200")