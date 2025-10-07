import math
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
x = (c*60+d)-(a*60+b)
if x <= 15:
  print("Pay:0")
elif x <=180 :
  y= math.ceil(x/60)
  print("Pay:",y*10)
elif x<=360:
  z=math.ceil(x/60)
  if z <=3:
   print("Pay:",z*10)
  else:
   print("Pay:",3*10 +(z-3)*20 )
else:
  print("Pay:200")