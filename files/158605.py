xh = int(input())
xm = int(input())
yh = int(input())
ym = int(input())
x = (xh*60)+xm
y = (yh*60)+ym
if y-x<=15:
    print("Pay:0")
elif y-x<=60:
    print("Pay:10")
elif y-x<=120:
    print("Pay:20")
elif y-x<=180:
    print("Pay:30")
elif y-x<=240:
    print("Pay:50")
elif y-x<=300:
    print("Pay:70")
else:
    print("Pay:200")