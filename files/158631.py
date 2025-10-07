HB = int(input())
MB = int(input())
HA = int(input())
MA = int(input())
total = ((HA*60)+MA)-((HB*60)+MB)
if total % 60 > 0:
    x = (total // 60)+1
else:
    x = total // 60
if total <= 15:
    print("pay:0")
elif total < 180:
    print("pay:",x*10, sep="")
elif total <= 360:
    print("pay:",((x-3)*20)+30, sep="")
else:
    print("pay:200")