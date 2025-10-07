a = int(input())
b = int(input())
c = int(input())
d = int(input())

o = c-a
p = b-d


    
if p <0:
  p = p*-1

if p <= 15 and o == 0:
    print("Pay:0")
elif p > 0:
    o = o+1
    
if o<4:
    p = p-p
    pay = o*10
    print(f"Pay:{pay}")
elif o<=3:
    print(f"Pay:{pay}")
elif o>=4 and o<=6:
    newo = 3
    newo = newo*10
    o = o-3
    newpay = newo + (o*20)
    print(f"Pay:{newpay}")
else:
    print("Pay:200")