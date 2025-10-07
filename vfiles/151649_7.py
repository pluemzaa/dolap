# รับค่า v1 และแปลงเป็น list ของ int ในบรรทัดเดียว
v1_str = input("Enter v1 (เช่น 1 2 3): ")
v1 = [int(num) for num in v1_str.split()]

# รับค่า v2 และแปลงเป็น list ของ int ในบรรทัดเดียว
v2_str = input("Enter v2 (เช่น 4 5 6): ")
v2 = [int(num) for num in v2_str.split()]

# ตรวจสอบว่าเวกเตอร์มี 3 มิติหรือไม่ (ป้องกัน error)
if len(v1) == 3 and len(v2) == 3:
    # คำนวณ dot product
    s = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    print(f"Dot product คือ: {s}")
else: