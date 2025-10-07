# รับค่าจำนวนเต็ม n จากผู้ใช้
try:
    n = int(input("Enter number: "))

    # ตรวจสอบว่า n มากกว่าหรือเท่ากับ 1 หรือไม่
    if n < 1:
        print("Error number must be 1 or greater")
    else:
        # วนลูปเพื่อสร้างแถว (i) จาก 0 ถึง n-1
        for i in range(n):
            # วนลูปเพื่อสร้างหลัก (j) จาก 0 ถึง n-1
            for j in range(n):
                # คำนวณหาตัวเลขที่จะแสดง
                # (i + j) % 9 จะได้ผลลัพธ์ในช่วง 0-8
                # + 1 เพื่อปรับช่วงเป็น 1-9
                num = ((i + j) % 9) + 1
                
                # แสดงผลตัวเลขตามด้วยเว้นวรรค และไม่ขึ้นบรรทัดใหม่
                print(num, end=" ")
            
            # เมื่อจบแต่ละแถว (จบลูป j) ให้ขึ้นบรรทัดใหม่
            print()

except ValueError:
    # กรณีผู้ใช้ป้อนค่าที่ไม่ใช่ตัวเลข
    print("Invalid input. Please enter an integer.")