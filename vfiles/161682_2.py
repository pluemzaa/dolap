import math

# รับ input เป็น string แล้วแปลงเป็น list ของ float
p_input = input("Enter coordinates of point P (p1, p2,...,pn): ")
q_input = input("Enter coordinates of point Q (q1, q2,...,qn): ")

p = list(map(float, p_input.split()))
q = list(map(float, q_input.split()))

# ตรวจสอบว่าขนาดเท่ากันไหม
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    distance = 0
    for i in range(len(p)):
        distance += (q[i] - p[i]) ** 2
    distance = math.sqrt(distance)
    print(f"Euclidean distance between point P and point Q {distance:.2f}")