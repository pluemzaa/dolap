import math

# รับค่าเวกเตอร์จากผู้ใช้
p = [float(x) for x in input("Enter coordinates of point P (p1, p2,...,qn): ").split(",")]
q = [float(x) for x in input("Enter coordinates of point Q (q1, q2,...,qn): ").split(",")]

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(p)):
        diff = p[i] - q[i]         # ผลต่าง
        total += diff ** 2         # บวกผลต่างกำลังสองสะสม
    distance = math.sqrt(total)    # หารากที่สอง
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")