import math

# รับ input เวกเตอร์ P
p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
# รับ input เวกเตอร์ Q
q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

# แปลง string เป็น list ของ float
p = list(map(float, p_input.strip().split()))
q = list(map(float, q_input.strip().split()))

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    distance = math.sqrt(sum((q[i] - p[i]) ** 2 for i in range(len(p))))
    # แสดงผลลัพธ์ตามฟอร์แมตเป๊ะ
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")