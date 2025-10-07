I_hours=int(input(""))
I_min=int(input(""))
O_hours=int(input(""))
O_min=int(input(""))
I_hormin=(I_hours*60)+I_min
O_houmin=(O_hours*60)+O_min
pay=O_houmin-I_hormin
if pay <= 15:
  print("pay:0")
elif pay <= 60:
  print("pay:10")
elif pay <= 120:
  print("pay:20")
elif pay <= 180:
  print("pay:30")
elif pay <= 240:
  print("pay:50")
elif pay <= 300:
  print("pay:70")
elif pay <= 360:
  print("pay:90")
else :
    print("pay:200")