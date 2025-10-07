4
i=int(input())#ชม ที่เข้ามา
q=int(input())#นาที ที่เข้ามา
e=int(input())#ชม ที่ออก
z=int(input())#นาที ที่ออก
A=int(((e*60)+z)-((i*60)+q))
if A<=15:
    print("Pay:0")
elif A<=60:
    print("Pay:10")
elif A<=120:
    print("Pay:20")
elif A<=180:
    print("Pay:30")
elif A<=240:
    print("Pay:50")
elif A<=300:
    print("Pay:70")
elif A<=360:
    print("Pay:90")
else:
    print("Pay:200")