A=int(input())#ชม.เข้า
B=int(input())#นาที เข้า
C=int(input())#ชม.ออก
D=int(input())#นาที ออก
A=A*60
C=C*60
if (C+D)-(A+B)<=15:
  print('Pay:0')
elif (C+D)-(A+B)<=60:
  print('Pay:10')
elif (C+D)-(A+B)<=180:
  print('Pay:30')
elif (C+D)-(A+B)<=360:
  print('Pay:50')
elif (C+D)-(A+B)>360:
  print('Pay:200')