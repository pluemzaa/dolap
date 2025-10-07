xh = int(input())
xm = int(input())
yh = int(input())
ym = int(input())
x = (xh*60)+xm
y = (yh*60)+ym
a = y-x
if a<=15:
  print("Pay:0")
elif a<=60:
  print("Pay:10")
elif a<=120:
  print("Pay:20")
elif a<=180:
  print("Pay:30")
elif a<=240:
  print("Pay:50")  
elif a<=300:
  print("Pay:70")
else:
  print("Pay:200")