x1= int(input())*60
x2= int(input())
x3= int(input())*60
x4= int(input())
z=(x4+x3)-(x1+x2)
a=(z//60)
if z%60 !=0:
    a=a+1

print(a)
if z <=15:
    print('pay:',a*0,sep='')
elif z>15 and z<=180  :
     print('pay:',a*10,sep="")
elif z>180 and z<=360 :
     print('pay:',((a-3)*20+30),sep="")
else :
     print('pay:',200,sep="")