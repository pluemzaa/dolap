import math

m = int(input())  # จำนวนไม้
k = int(input())  # ลูกชิ้นต่อไม้
n = int(input())  # ลูกชิ้นต่อถุง

total_needed = m * k
bags = math.ceil(total_needed / n)
print(bags)