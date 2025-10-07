import math
x = int(input())
y = int(input())
z = int(input())
w = int(input())
M = (z*60-x*60)+(w-y)
if M<=15:
  print("Pay:0")
elif M<=180:
    H = math.ceil(M/60)
    H1 = H*10
    print("Pay:", H1, sep="")
elif M>=181 and M<=360:
    Hs = math.ceil(M/60)
    Hs2 = (3*10)+((Hs-3)*20)
    print("Pay:", Hs2, sep="")
else:
  print("Pay:200")