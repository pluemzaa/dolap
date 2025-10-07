in_hr = int(input())
in_min = int(input())
out_hr = int(input())
out_min = int(input())

time_in = in_hr * 60 + in_min
time_out = out_hr * 60 + out_min
time_total = time_out - time_in
if (in_hr < 7 ) or (out_hr > 23) or (time_total < 0):
    print("ยังไม่เปิดบริการ")
elif time_total <= 15 :
    print("Pay:0")
elif time_total <= 180
    print("Pay:",((time_total + 59) // 60) * 10)
elif time_total <= 360 :
    hr + (time_total + 59) // 60
    print("Pay:",(30 + (hr-3)*20))
else:
    print("Pay:200")