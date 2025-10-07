import math

m = int(input("กรุณาใส่จำนวนไม้ที่ลูกค้าสั่ง: "))  
k = int(input("กรุณาใส่จำนวนลูกชิ้นต่อไม้: "))  
n = int(input("กรุณาใส่จำนวนลูกชิ้นต่อถุง: "))     

total_meatballs = m * k

bags_needed = math.ceil(total_meatballs / n)

print(int(bags_needed))