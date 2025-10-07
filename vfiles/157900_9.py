Hin = int(input())
Min = int(input())
Hout = int(input())
Mout = int(input())
TotalTime = ((Hout*60)+Mout) - ((Hin*60)+Min)
print(TotalTime)

if TotalTime % 60 == 0:
    TotalHours = TotalTime // 60
else:
    TotalHours = TotalTime // 60 + 1

if TotalHours <= 3:
    Pay = TotalHours * 10
elif TotalHours <= 6:
    Pay = 30 + (TotalHours - 3) * 20
else:
    Pay = 200
print("Pay:", Pay)