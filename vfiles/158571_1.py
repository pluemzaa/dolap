# รับข้อมูลเวลาที่เข้าและออก
in_hour = int(input())
in_minute = int(input())
out_hour = int(input())
out_minute = int(input())

# แปลงเวลาเข้า-ออกเป็นนาทีทั้งหมดจากเที่ยงคืน
in_total = in_hour * 60 + in_minute
out_total = out_hour * 60 + out_minute

# คำนวณเวลาจอดรถเป็นนาที
duration = out_total - in_total

# เช็คเงื่อนไขคิดค่าบริการ
if duration <= 15:
    pay = 0
elif duration <= 180:  # ไม่เกิน 3 ชั่วโมง
    # คิดชั่วโมง (ปัดเศษขึ้น)
    hours = (duration + 59) // 60
    pay = hours * 10
elif duration <= 360:  # ตั้งแต่ 4 ถึง 6 ชั่วโมง (240-360 นาที)
    # คิดชั่วโมงทั้งหมด (ปัดเศษขึ้น)
    total_hours = (duration + 59) // 60
    # ชั่วโมงแรก 3 ชั่วโมง คิด 10 บาท/ชั่วโมง
    first_3 = 3 * 10
    # ชั่วโมงที่ 4-6 คิด 20 บาท/ชั่วโมง
    next_hours = total_hours - 3
    pay = first_3 + next_hours * 20
else:
    pay = 200  # เกิน 6 ชั่วโมงเหมาจ่าย

print(f"Pay:{pay}")