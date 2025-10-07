import math

# รับ input จากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลง input เป็น list ของตัวเลข
try:
    p = [float(x) for x in p_input.split(',')]
    q = [float(x) for x in q_input.split(',')]
except ValueError:
    print("Error: Please enter valid numbers separated by commas")
    exit()

# ตรวจสอบว่าเวกเตอร์มีขนาดเท่ากันหรือไม่
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณระยะ Euclidean
    distance = math.sqrt(sum((q[i] - p[i]) ** 2 for i in range(len(p))))
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")