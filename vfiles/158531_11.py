# รับค่าตัวเลขจากผู้ใช้
number = int(input("Enter a number: "))

# ตรวจสอบค่าที่รับมา
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")