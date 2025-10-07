import math

# รับ input ตาม format ที่กำหนด
p = list(map(float, input("Enter coordinates of point P (p1, p2,...,qn): ").split(",")))
q = list(map(float, input("Enter coordinates of point Q (q1, q2,..., qn): ").split(",")))

# ตรวจสอบความยาวของเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_sq = 0
    for i in range(len(p)):
        sum_sq += (p[i] - q[i]) ** 2
    distance = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")