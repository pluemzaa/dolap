# รับข้อมูลจากผู้ใช้
member = input("Membership (y/n) : ").lower()
total = float(input("Total amount : "))

# กำหนดส่วนลดเริ่มต้น
discount = 0.0

# ตรวจสอบเงื่อนไข
if member == 'y':
    if total >= 1000:
        discount = total * 0.20
    elif total >= 500:
        discount = total * 0.10
elif member == 'n':
    if total >= 1000:
        discount = total * 0.05

# คำนวณราคาสุทธิ
final_amount = total - discount

# แสดงผลลัพธ์
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")