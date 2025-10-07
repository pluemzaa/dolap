# รับข้อมูลเวลาเข้า
in_hour = int(input())
in_minute = int(input())

# รับข้อมูลเวลาออก
out_hour = int(input())
out_minute = int(input())

# แปลงเวลาเข้าและออกเป็นจำนวนนาทีทั้งหมด
in_total = in_hour * 60 + in_minute
out_total = out_hour * 60 + out_minute

# คำนวณเวลาที่จอดรถ (นาที)
duration = out_total - in_total

# ตรวจสอบเงื่อนไขและคำนวณค่าจอดรถ
if duration <= 15:
    fee = 0
elif duration <= 180:  # ไม่เกิน 3 ชั่วโมง
    hours = (duration + 59) // 60  # ปัดเศษขึ้น
    fee = hours * 10
elif duration <= 360:  # 4-6 ชั่วโมง
    # ชั่วโมงแรกถึง 3 ชั่วโมง = 3 * 10 = 30 บาท
    remaining_minutes = duration - 180
    extra_hours = (remaining_minutes + 59) // 60
    fee = 30 + extra_hours * 20
else:  # เกิน 6 ชั่วโมง
    fee = 200

# แสดงผลลัพธ์
print("Pay:" + str(fee))