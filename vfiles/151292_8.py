def calculate_dot_product():
    """
    คำนวณ Dot Product ของเวกเตอร์สองเวกเตอร์ที่มีสมาชิก 3 ตัว
    ที่ผู้ใช้ป้อนเข้ามา
    """
    print("โปรแกรมคำนวณ Dot Product")

    # รับข้อมูลเวกเตอร์ v1 จากผู้ใช้
    while True:
        try:
            v1_str = input("Enter v1 (space-separated): ")
            v1 = [int(x) for x in v1_str.split()]
            if len(v1) != 3:
                print("Error: v1 ต้องมีสมาชิก 3 ตัว กรุณาป้อนใหม่")
            else:
                break
        except ValueError:
            print("Error: รูปแบบข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลขเท่านั้น")

    # รับข้อมูลเวกเตอร์ v2 จากผู้ใช้
    while True:
        try:
            v2_str = input("Enter v2 (space-separated): ")
            v2 = [int(x) for x in v2_str.split()]
            if len(v2) != 3:
                print("Error: v2 ต้องมีสมาชิก 3 ตัว กรุณาป้อนใหม่")
            else:
                break
        except ValueError:
            print("Error: รูปแบบข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลขเท่านั้น")

    # คำนวณ Dot Product
    dot_product = 0
    for i in range(3):
        dot_product += v1[i] * v2[i]

    # แสดงผลลัพธ์
    print(f"Dot product: {dot_product}")

# เรียกใช้ฟังก์ชัน
calculate_dot_product()