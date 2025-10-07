import math

# ฟังก์ชันในการคำนวณ Euclidean distance
def calculate_euclidean_distance(p, q):
    if len(p) != len(q):
        print("Error: Vectors must have the same size")
        return None
    # คำนวณระยะห่าง
    distance = math.sqrt(sum((q[i] - p[i]) ** 2 for i in range(len(p))))
    return distance

# ส่วนหลักของโปรแกรม
while True:
    # รับค่าพิกัดของจุด P
    numbers_p = input("Enter coordinates of point P (p1, p2,..., qn): ").split(',')
    p = [int(x) for x in numbers_p]  # แปลงพิกัดให้เป็นตัวเลข

    # รับค่าพิกัดของจุด Q
    numbers_q = input("Enter coordinates of point Q (q1, q2,..., qn): ").split(',')
    q = [int(i) for i in numbers_q]  # แปลงพิกัดให้เป็นตัวเลข

    # คำนวณระยะห่าง
    distance = calculate_euclidean_distance(p, q)
    
    # ถ้าผลลัพธ์ไม่ใช่ None (กรณีมีขนาดเท่ากัน)
    if distance is not None:
        # แสดงผลลัพธ์
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")
    
    # ถามผู้ใช้ว่าจะกรอกข้อมูลต่อหรือไม่
    continue_input = input("Do you want to enter more coordinates? (y/n): ").strip().lower()
    if continue_input != 'y':
        break  # ออกจากลูปเมื่อกรอกเสร็จ