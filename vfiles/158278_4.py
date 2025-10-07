in_hr = int(input())
in_min = int(input())
out_hr = int(input())
out_min = int(input())
hr = out_hr - in_hr
min = out_min - in_min
if hr == 0 and min <= 15:
  print("Pay:0")
elif (hr == 0 and min > 15) or (hr < 3 and min > 0):
  if (hr == 0 and min > 15) or (hr == 1 and min == 0):
    print("Pay:10")
  elif (hr == 1 and min > 0) or (hr == 2 and min == 0):
    print("Pay:20")
  elif (hr == 2 and min > 0) or (hr == 3 and min == 0):
    print("Pay:30")
elif (hr >= 3 and min > 0) or (hr <= 6 and min == 0):
  if (hr == 3 and min > 0) or (hr == 4 and min == 0):
    print("Pay:50")
  elif (hr == 4 and min > 0) or (hr == 5 and min == 0):
    print("Pay:70")
  elif (hr == 5 and min > 0) or (hr == 6 and min == 0):
    print("Pay:90")
else:
  print("Pay:200")