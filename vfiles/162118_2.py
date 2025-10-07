import math

# รับข้อมูลเวกเตอร์
q_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
p_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงเป็นลิสต์ของจำนวนเต็ม
q = list(map(int, q_input.split(',')))
p = list(map(int, p_input.split(',')))

# ตรวจสอบขนาดของเวกเตอร์
if len(q) != len(p):
    print("Error: Vectors must have the same size")
else:
    sum_square = 0
    for i in range(len(q)):
        diff = q[i] - p[i]
        sum_square += diff ** 2

    distance = math.sqrt(sum_square)
    print(f"Euclidean distance between point P and point Q: = {distance:.2f}")