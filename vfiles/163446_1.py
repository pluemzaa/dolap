import math

m = int(input())  # จำนวนไม้ที่ลูกค้าสั่ง
k = int(input())  # จำนวนลูกชิ้นต่อไม้
n = int(input())  # จำนวนลูกชิ้นใน 1 ถุง

total_balls = m * k

bags = math.ceil(total_balls / n)

print(bags)