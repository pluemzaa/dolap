import math

# รับค่าพิกัดของ P และ Q
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงเป็น list ของตัวเลข
P = [float(x) for x in p_input.split(",")]
Q = [float(x) for x in q_input.split(",")]

# ตรวจสอบว่าขนาดเวกเตอร์เท่ากัน
if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(P)):
        diff = P[i] - Q[i]
        squared = diff ** 2
        total += squared
    distance = math.sqrt(total)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")