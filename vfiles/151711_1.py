v1_input = input("Enter v1 (space-separated): ")
v2_input = input("Enter v2 (space-separated): ")

# แปลงข้อมูลที่รับมาให้เป็นลิสต์ของจำนวนเต็ม
v1 = list(map(int, v1_input.split()))
v2 = list(map(int, v2_input.split()))

# ตรวจสอบว่าแต่ละเวกเตอร์มีสมาชิก 3 ตัว
if len(v1) != 3 or len(v2) != 3:
    print("แต่ละเวกเตอร์ต้องมีสมาชิก 3 ตัวเท่านั้น")
else:
    # คำนวณ dot product
    dot_product = sum(a * b for a, b in zip(v1, v2))
    print("Dot product:", dot_product)