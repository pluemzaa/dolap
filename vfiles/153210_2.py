print('Hello Python!')# รับค่าเวกเตอร์ v1 จากผู้ใช้
v1_str = input("Enter v1 (space-separated): ")
v1 = [int(x) for x in v1_str.split()] # แปลงข้อความเป็นลิสต์ของ
v2_str = input("Enter v2 (space-separated): ")
v2 = [int(x) for x in v2_str.split()] # แปลงข้อความเป็นลิสต์ของตัวเลข

dot_product_result = (v1[0] * v2[0]) + \
                     (v1[1] * v2[1]) + \
                     (v1[2] * v2[2])
print(f"Dot product: {dot_product_result}")