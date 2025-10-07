import math

# รับข้อมูลเวกเตอร์ P และ Q
p_input = input("Enter coordinates of point P (p1, p2,..., qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงข้อมูลที่ป้อนให้เป็น list ของตัวเลข (float)
p = [float(x) for x in p_input.split(",")]
q = [float(x) for x in q_input.split(",")]

# ตรวจสอบว่าขนาดเวกเตอร์เท่ากันหรือไม่
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    sum_sq = 0
    for i in range(len(p)):
        sum_sq += (p[i] - q[i]) ** 2
    distance = math.sqrt(sum_sq)
    
    # แสดงผลลัพธ์ทศนิยม 2 ตำแหน่ง
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")