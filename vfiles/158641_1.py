w = int(input())
x = int(input())
y = int(input())
z = int(input())
ww = (w*60)+x
yy = (y*60)+z
pay = yy-ww
if pay <= 15:
  print("pay:0")
elif pay <= 60:
  print("pay:10")
elif pay <= 120:
  print("pay:20")
elif pay <= 180:
  print("pay:30")
elif pay <= 240:
  print("pay:50")
elif pay <= 300:
  print("pay:70")
else:
  print("pay:200")