Hrin = int(input())
Miin = int(input())
Hrout = int(input())
Miout = int(input())
Thr = Hrout - Hrin
Thr = Thr*60
if Miin == Miout:
    Tmi = 0
else:
    Tmi = Miout + Miin
Alltime = Thr + Tmi
Thr = Thr//60
Tmi = Tmi%60
Cost = 0
if Tmi >= 60:
  Thr = Thr+1
  Tmi = Tmi-60
if Tmi <= 15 and Thr == 0:
    Cost = Cost + 0
elif Thr < 3 and Tmi >15:
    if Tmi != 0:
        Tmi = 1
    Cost = Cost + (Thr * 10) + (Tmi * 10)
elif Thr <= 3 :
    if Tmi != 0:
        Tmi = 1
    Cost = Cost + (Thr * 10) + (Tmi * 20)
if Thr >= 4 and Thr < 6:
    if Tmi != 0:
        Tmi = 1
    Cost = Cost + ((Thr - 3) * 20)
elif Thr >= 6 :
    Cost = Cost + 200
print("Pay:",Cost)