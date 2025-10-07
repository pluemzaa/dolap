Hin = int(input())
Min = int(input())
Hout = int(input())
Mout = int(input())
TotalTime = ((Hout*60)+Mout) - ((Hin*60)+Min)

if TotalTime % 60 == 0:
    TotalHours = TotalTime // 60
else:
    TotalHours = TotalTime // 60 + 1

if TotalTime <= 15:
    print("Pay:0")
elif TotalHours <= 3:
    Pay = TotalHours * 10
    print (f"Pay:{Pay}")
elif TotalHours <= 6:
    Pay = 30 + (TotalHours - 3) * 20
    print (f"Pay:{Pay}")
else:
    print("Pay:200")