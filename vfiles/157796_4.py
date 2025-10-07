h = int(input())
m = int(input())
h2 = int(input())
m2 = int(input())
min = h*60
min2 = h2*60
minute = min+m
minute2 = min2+m2
l = minute2-minute
c = l//60
d = l%60
if d!=0:
    d=1
else:
    d=0
if l<16:
    print("Pay:0")
elif l>15 and l<=180 :
    c+=d
    print("Pay:",c*10)
elif l>180 and l<359:
    c+=d
    print("Pay:",30+((c-3)*20))
else:
    print("Pay:200")