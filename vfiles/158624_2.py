A=int(input())
B=int(input())
C=int(input())
D=int(input())
A=A*60
C=C*60
if (C+D)-(A+B)<=15:
  print("Pay:0")
elif (C+D)-(A+B)<=179:
  print("Pay:10")
elif (C+D)-(A+B)<=240:
  print("Pay:30")
elif (C+D)-(A+B)<=360:
  print("Pay:50")
elif (C+D)-(A+B)>360:
  print("Pay:200")