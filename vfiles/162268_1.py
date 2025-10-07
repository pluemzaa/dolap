import math

# รับเวกเตอร์จากผู้ใช้และแปลงเป็น list ของจำนวนเต็ม
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# แปลงข้อมูลเป็น list โดยลบช่องว่างข้างๆ
p = [int(x.strip()) for x in p_input.split(",") if x.strip() != ""]
q = [int(x.strip()) for x in q_input.split(",") if x.strip() != ""]

# ตรวจสอบขนาดเวกเตอร์
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    # คำนวณผลต่างกำลังสองของแต่ละมิติ
    sum_of_squares = 0
    for pi, qi in zip(p, q):
        diff = pi - qi
        sum_of_squares += diff ** 2
    # หารากที่สอง
    distance = math.sqrt(sum_of_squares)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")