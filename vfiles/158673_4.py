x1=int(input())
x2=int(input())
x3=int(input())
x4=int(input())
x11= int(((x3*60)+x4)-((x1*60)+x2))
if x11<=15:
  print("Pay:0")
elif x11<=60:
  print("Pay:10")
elif x11<=120:
  print("Pay:20")
elif x11<=180:
  print("Pay:30")
elif x11<=240:
  print("Pay:50")
elif x11<=300:
  print("Pay:70")
elif x11<=360:
  print("Pay:90")
else:
  print("Pay:200")