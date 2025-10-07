import math

# รับ input แบบเว้นวรรค
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลงเป็น list ของ float
p = list(map(float, p_input.strip().split()))
q = list(map(float, q_input.strip().split()))

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    distance = math.sqrt(sum((q[i] - p[i]) ** 2 for i in range(len(p))))
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")