# รับค่าตัวเลขจากผู้ใช้
number = float(input("Enter a number: "))

# ตรวจสอบค่าที่รับมา
if number >= 0:
    print(f"{number} is greater than or equal 0")
else:
    print(f"{number} is less than 0")