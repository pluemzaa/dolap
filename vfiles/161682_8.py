import math

# รับค่า input จากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลงข้อมูลเป็น list ของ float
p = list(map(float, p_input.split(',')))
q = list(map(float, q_input.split(',')))

# ตรวจสอบความยาวของเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    distance = math.sqrt(sum((qi - pi) ** 2 for pi, qi in zip(p, q)))
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")