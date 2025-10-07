import math

# รับค่าพิกัด P
p_input = input("Enter coordinates of point P (p1, p2, ..., pn): ")
# รับค่าพิกัด Q
q_input = input("Enter coordinates of point Q (q1, q2, ..., qn): ")

# แปลง string -> list ของ float
p = list(map(float, p_input.split(',')))
q = list(map(float, q_input.split(',')))

# ตรวจสอบว่ามีจำนวนสมาชิกเท่ากันหรือไม่
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณ Euclidean distance
    distance = math.sqrt(sum((q[i] - p[i])**2 for i in range(len(p))))
    # แสดงผลลัพธ์ทศนิยม 2 ตำแหน่ง
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")