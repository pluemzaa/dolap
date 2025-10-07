v1_input = input("Enter v1 (space-separated): ")
v2_input = input("Enter v2 (space-separated): ")

# แปลงข้อมูลที่รับเข้ามาเป็น list ของจำนวนเต็ม
v1 = list(map(int, v1_input.split()))
v2 = list(map(int, v2_input.split()))

# ตรวจสอบว่ามีสมาชิก 3 ตัวหรือไม่
if len(v1) != 3 or len(v2) != 3:
    print("แต่ละเวกเตอร์ต้องมีสมาชิก 3 ตัวเท่านั้น")
else:
    # คำนวณ Dot product
    dot_product = sum(v1[i] * v2[i] for i in range(3))
    print(f"Dot product: {dot_product}")