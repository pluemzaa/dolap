import math

# รับเวกเตอร์ P และ Q จากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลงสตริงเป็น list ของ float
p = list(map(float, p_input.split()))
q = list(map(float, q_input.split()))

# ตรวจสอบความยาว
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    distance = math.sqrt(sum((q[i] - p[i]) ** 2 for i in range(len(p))))
    print(f"Euclidean distance between point P and point Q {distance:.2f}")