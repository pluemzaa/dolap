# รับค่าตัวเลขจากผู้ใช้
number = int(input("Enter a number: "))

# ตรวจสอบว่าเป็นค่ามากกว่าหรือเท่ากับ 0 หรือน้อยกว่า 0
if number >= 0:
    print(f"{number} is greater than or equal 0")
else:
    print(f"{number} is less than 0")