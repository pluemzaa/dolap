# รับค่าปีจากแป้นพิมพ์
year = int(input("Enter any year that is to be checked for leap year: "))

# ตรวจสอบเงื่อนไขของปีอธิกสุรทิน
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")