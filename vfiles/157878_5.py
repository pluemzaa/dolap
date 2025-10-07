# รับค่าปีจากผู้ใช้
year = int(input("Enter any year that is to be checked for leap year: "))

# ตรวจสอบว่าเป็นปีอธิกสุรทินหรือไม่
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The given year is a leap year")
else:
    print("It is not a leap year")