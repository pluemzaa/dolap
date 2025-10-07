import math

# รับข้อมูลเวกเตอร์
q_input = input("Enter vector q (comma-separated): ")
p_input = input("Enter vector p (comma-separated): ")

# แปลงเป็นลิสต์ของจำนวนเต็ม
q = list(map(int, q_input.split(',')))
p = list(map(int, p_input.split(',')))

# ตรวจสอบขนาดของเวกเตอร์
if len(q) != len(p):
    print("Error: Vectors must be of the same length")
else:
    sum_square = 0
    for i in range(len(q)):
        diff = q[i] - p[i]
        sum_square += diff ** 2

    distance = math.sqrt(sum_square)
    print(f"Euclidean distance = {distance:.2f}")