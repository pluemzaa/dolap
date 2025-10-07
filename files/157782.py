hour_in = int(input(""))
minute_in = int(input(""))
hour_out = int(input(""))
minute_out = int(input(""))

time_in = hour_in * 60 + minute_in
time_out = hour_out * 60 + minute_out

time_parked = time_out - time_in


if time_parked <= 15:
    pay = 0
elif time_parked <= 180:
    pay = ((time_parked + 59) // 60) * 10  
elif time_parked <= 360:
    time_above_180 = time_parked - 180  # เวลาที่จอดเกิน 3 ชั่วโมง
    pay = (180 // 60) * 10 + ((time_above_180 + 59) // 60) * 20
else:
    pay = 200  # เหมาจ่ายวันละ 200 บาท

# แสดงผลลัพธ์
print(f"Pay:{pay}")