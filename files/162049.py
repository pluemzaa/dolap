# รับค่าจากผู้ใช้
n = int(input("Enter number: "))

# ตรวจสอบเงื่อนไขว่า n ต้องมากกว่าหรือเท่ากับ 1
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):  # วนลูปแต่ละแถว
        for j in range(n):  # วนลูปแต่ละคอลัมน์
            num = (i + j + 1) % 9  # คำนวณค่าตัวเลข
            if num == 0:
                num = 9
            print(num, end=" ")
        print()  # ขึ้นบรรทัดใหม่หลังจากพิมพ์ครบ 1 แถว