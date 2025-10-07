Hc=int(input())
Mc=int(input())
He=int(input())
Me=int(input())
Th = (He-Hc)*60
Tm = Me-Mc
M=Th+Tm
if M<=15:
    print("Pay: 0")
elif M>15 and M<=180:
    a = (M/60)
    P1 = int(a) + (a != int(a))
    Price1 = P1*10
    print("Pay:",Price1)
elif M>180 and M<=360:
    a = (M/60)
    P2 = int(a) + (a != int(a))
    Price2 = (P2*20)-30
    print("Pay:",Price2)
else:
    print("Pay: 200")