in_hr = int(input(""))
in_min = int(input(""))
out_hr = int(input(""))
out_min = int(input(""))
min_in = in_hr * 60 + in_min
min_out = out_hr * 60 + out_min
min = min_out - min_in
if min <= 15:
  print("Pay:0")
elif min > 15 and min <= 60: 
  print("Pay:10")
elif min > 60 and min <= 120:
  print("Pay:20")
elif min > 120 and min <= 180:
  print("Pay:30")
elif min > 180 and min <= 240:
  print("Pay:50")
elif min > 240 and min <= 300:
  print("Pay:70")
elif min > 300 and min <= 360:
  print("Pay:90")
else :
  print("Pay:200")