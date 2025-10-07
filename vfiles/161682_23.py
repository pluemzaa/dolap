import math

# รับเวกเตอร์ P
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
# รับเวกเตอร์ Q
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลงเวกเตอร์เป็น list
p = list(map(float, p_input.strip().split()))
q = list(map(float, q_input.strip().split()))

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    total = 0
    for i in range(len(p)):
        total += (q[i] - p[i]) ** 2
    distance = math.sqrt(total)
    print("Euclidean distance between point P and point Q:", format(distance, ".2f"))