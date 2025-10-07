import math

# รับข้อมูลจากผู้ใช้
m = int(input())  # จำนวนไม้ที่ลูกค้าสั่ง
k = int(input())  # จำนวนลูกชิ้นต่อไม้
n = int(input())  # จำนวนลูกชิ้นใน 1 ถุง

# คำนวณ
total_meatballs = m * k
bags_needed = math.ceil(total_meatballs / n)

# แสดงผล
print(bags_needed)