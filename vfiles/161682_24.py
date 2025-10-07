import math

# รับค่าเวกเตอร์ P
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
# รับค่าเวกเตอร์ Q
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลงค่าที่รับมาเป็น list ของ float
p = list(map(float, p_input.strip().split()))
q = list(map(float, q_input.strip().split()))

# ตรวจสอบว่าเวกเตอร์มีขนาดเท่ากันหรือไม่
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    d = 0
    for i in range(len(p)):
        d += (q[i] - p[i]) ** 2
    d = math.sqrt(d)
    print("Euclidean distance between point P and point Q:", '%.2f' % d)