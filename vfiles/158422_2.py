num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
x=60*(num3-num1)+(num4-num2)
if x<=15:
    print("Pay:0")
elif x%60:
    x=x+60
if x>15 and x<=180:
    print('Pay:',10*(x//60))
if x>180 and x<=360:
    print('Pay:',30+20*((x-180)//60))
if x>360:
    print("Pay:200")