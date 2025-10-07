# รับเวกเตอร์ตัวแรก
v1_str = input("Enter v1 (space-separated): ")
v1 = v1_str.split(" ")

# รับเวกเตอร์ตัวที่สอง
v2_str = input("Enter v2 (space-separated): ")
v2 = v2_str.split(" ")

# ตรวจสอบจำนวนสมาชิกทั้งสองเวกเตอร์ต้องเป็น 3 ตัว
if len(v1) != 3 or len(v2) != 3:
    print("Each vector must have exactly 3 elements.")
else:
    # แปลงข้อมูลเป็นจำนวนเต็ม
    v1 = [int(x) for x in v1]
    v2 = [int(x) for x in v2]

    # คำนวณ Dot Product
    dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

    # แสดงผล
    print("Dot product:", dot_product)