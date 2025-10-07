import math

# รับค่าจากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลง string เป็น list ของตัวเลข
p = [float(x.strip()) for x in p_input.split(",")]
q = [float(x.strip()) for x in q_input.split(",")]

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    sum_sq = 0
    for i in range(len(p)):
        sum_sq += (q[i] - p[i]) ** 2
    d = math.sqrt(sum_sq)

    print(f"Euclidean distance between point P and point Q: {d:.2f}")