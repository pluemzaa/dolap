# รับข้อมูลประเภทรถและจำนวนชั่วโมงจากผู้ใช้
try:
    vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))
except ValueError:
    # ดักจับกรณีที่ผู้ใช้ป้อนข้อมูลที่ไม่ใช่ตัวเลข
    print("Invalid input. Please enter numbers only.")
    exit() # จบการทำงาน

# --- ตรวจสอบความถูกต้องของข้อมูล ---

# 1. ตรวจสอบว่าประเภทรถเป็น 1 หรือ 2 เท่านั้น
if vehicle_type not in [1, 2]:
    print("Invalid vehicle type")
    exit()

# 2. ตรวจสอบว่าจำนวนชั่วโมงที่ป้อนต้องมากกว่า 0
if hours <= 0:
    print("Please enter a valid number of parking hours")
    exit()

# --- คำนวณค่าจอดรถ ---

parking_fee = 0.0

# กรณีที่ 1: จอดไม่ถึง 1 ชั่วโมง (จอดฟรี)
if hours < 1:
    parking_fee = 0.0
# กรณีที่ 2: รถจักรยานยนต์
elif vehicle_type == 1:
    # ชั่วโมงแรก 10 บาท + ชั่วโมงที่เหลือชั่วโมงละ 5 บาท
    parking_fee = 10 + (hours - 1) * 5
# กรณีที่ 3: รถยนต์ส่วนบุคคล
elif vehicle_type == 2:
    # ชั่วโมงแรก 30 บาท + ชั่วโมงที่เหลือชั่วโมงละ 15 บาท
    parking_fee = 30 + (hours - 1) * 15

# --- แสดงผลลัพธ์ ---
# จัดรูปแบบผลลัพธ์เป็นทศนิยม 2 ตำแหน่ง
print(f"Parking fee: {parking_fee:.2f} THB")