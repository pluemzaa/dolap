import math

# รับค่าจากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,..., qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงข้อความที่รับเข้ามาให้เป็นลิสต์ของตัวเลข
try:
    p = [float(x.strip()) for x in p_input.split(",")]
    q = [float(x.strip()) for x in q_input.split(",")]
except ValueError:
    print("Error: Please enter valid numbers separated by commas.")
    exit()

# ตรวจสอบขนาดของเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    sum_sq = 0
    for i in range(len(p)):
        diff = p[i] - q[i]
        sum_sq += diff ** 2
    distance = math.sqrt(sum_sq)

    # แสดงผลลัพธ์โดยปัดทศนิยม 2 ตำแหน่ง
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")