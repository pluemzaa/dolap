import math

# รับข้อมูลจากผู้ใช้
p = input("Enter coordinates of point P (p1, p2,..., qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงเป็น list ของตัวเลข
p_list = [float(x) for x in p.split(",")]
q_list = [float(x) for x in q.split(",")]

# ตรวจสอบว่าขนาดเท่ากันหรือไม่
if len(p_list) != len(q_list):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    sum_sq = 0
    for i in range(len(p_list)):
        diff = p_list[i] - q_list[i]
        sum_sq += diff ** 2

    distance = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")