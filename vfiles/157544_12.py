import math
x1= int(input())*60
x2= int(input())
x3= int(input())*60
x4= int(input())
z=(x4+x3)-(x1+x2)
a=z/60
a=math.ceil(a)
if z <=15:
    print('pay:',a*0)
elif z>15 and z<=180  :
     print('pay:',a*10)
elif z>180 and z<=360 :
     print('pay:',((a-3)+30))
else :
     print('pay:',200)