hourin = int(input())
minin = int(input())
hourout = int(input())
minout = int(input())
total = ((hourout*60)+minout)-((hourin*60)+minin)
if total % 60 >0:
    x = (total // 60)+1
else:
        x = (total // 60)
if total <= 15:
    print("Pay:0")
elif total < 180:
    print("Pay:{}".format((x*10)))
elif total <= 360:
    print("Pay:{}".format((((x-3)*20)+30)))
else:
    print("Pay:200")