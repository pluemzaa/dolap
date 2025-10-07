import math

m = int(input())     # จำนวนไม้ที่ลูกค้าสั่ง
k = int(input())     # จำนวนลูกชิ้นต่อไม้
n = int(input())     # จำนวนลูกชิ้นใน 1 ถุง

total = m * k        # ลูกชิ้นที่ต้องใช้ทั้งหมด
bags = math.ceil(total / n)  # ถุงที่ต้องใช้ (ปัดขึ้น)

print(bags)