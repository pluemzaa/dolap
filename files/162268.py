import math  # เรียกใช้โมดูลสำหรับคณิตศาสตร์ จะใช้ฟังก์ชัน sqrt

# 1. รับข้อมูลเวกเตอร์ P จากผู้ใช้
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
# 2. รับข้อมูลเวกเตอร์ Q จากผู้ใช้
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

# 3. แปลงข้อมูลที่รับมา ให้เป็น list ของจำนวนเต็ม
# (ใช้ split(',') เพื่อแยกแต่ละมิติด้วย ',')
p_str_list = p_input.split(",")
q_str_list = q_input.split(",")

# 4. ตรวจสอบว่าทั้งสองเวกเตอร์มีขนาดเท่ากันหรือไม่
if len(p_str_list) != len(q_str_list):
    print("Error: Vectors must have the same size")
else:
    # 5. สร้าง list สำหรับเก็บค่าของแต่ละเวกเตอร์ (แปลงเป็นเลขจำนวนเต็ม)
    p = []
    q = []
    for i in range(len(p_str_list)):
        p.append(int(p_str_list[i].strip()))
        q.append(int(q_str_list[i].strip()))

    # 6. คำนวณผลรวมของผลต่างกำลังสอง
    sum_squares = 0
    for i in range(len(p)):
        diff = p[i] - q[i]         # หาค่าต่างของแต่ละมิติ
        diff_square = diff ** 2    # ยกกำลังสอง
        sum_squares += diff_square # บวกสะสม

    # 7. คำนวณหารากที่สองของผลรวมข้างต้น
    distance = math.sqrt(sum_squares)

    # 8. แสดงผลลัพธ์โดยปัดเป็นทศนิยม 2 ตำแหน่ง
    print("Euclidean distance between point P and point Q: %.2f" % distance)