import math

# รับ input
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แยกเวกเตอร์ด้วย comma
p = list(map(float, p_input.split(',')))
q = list(map(float, q_input.split(',')))

# ตรวจสอบความยาวของเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    d = 0
    for i in range(len(p)):
        d += (q[i] - p[i]) ** 2
    d = math.sqrt(d)
    print("Euclidean distance between point P and point Q: %.2f" % d)