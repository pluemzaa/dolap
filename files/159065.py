x1=int(input())
x2=int(input())
x3=int(input())
x4=int(input())
x11= int(((x3*60)+x4)-((x1*60)+x2))
if x11<=15:
  print("pay:0")
elif x11<=60:
  print("pay:10")
elif x11<=120:
  print("pay:20")
elif x11<=180:
  print("pay:30")
elif x11<=240:
  print("pay:50")
elif x11<=300:
  print("pay:70")
elif x11<=360:
  print("pay:90")
else:
  print("pay:200")