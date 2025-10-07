in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())
time_in = in_hour * 60 + in_minute
time_out = out_hour * 60 + out_minute
time_total = time_out - time_in
if (in_hour < 7) or (out_hour > 23) or (time_total < 0):
  print("ยังไม่เปิดบริการ")
elif time_total <= 15:
  print("Pay:0")
elif time_total < 180:
  print("Pay:",((time_total + 59) // 60) * 10)
elif time_total <= 360:
  hour = (time_total + 59) // 60
  print("Pay:",(30 + (hour - 3) * 20))
else:
  print("Pay:200")