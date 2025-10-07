# รับค่าจากผู้ใช้
n = int(input("Enter number: "))

# ตรวจสอบว่า n ต้องมากกว่าหรือเท่ากับ 1
if n < 1:
    print("Error number must be 1 or greater")
else:
    # วนลูปแต่ละแถว
    for i in range(n):
        # วนลูปแต่ละหลักในแถว
        for j in range(n):
            value = (i + j + 1) % 9  # คำนวณค่า (เริ่มจาก i+1, j=0)
            if value == 0:
                value = 9
            print(value, end=" ")
        print()  # ขึ้นบรรทัดใหม่