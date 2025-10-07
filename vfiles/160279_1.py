# รับค่าตัวเลขจากผู้ใช้ โดยคั่นด้วย ,
input_str = input("Enter a series of numbers separated by commas: ")

# แยกค่าด้วย comma แล้วแปลงเป็น int ทีละตัว
numbers = input_str.split(',')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])  # แปลงเป็นตัวเลข

# ตั้งค่าตัวแรกเป็นค่าสูงสุดเริ่มต้น
maximum = numbers[0]

# วนลูปเช็คค่าที่เหลือ
for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        print("set the maximum value to", maximum)

# แสดงค่ามากที่สุดสุดท้าย
print("The maximum value is", maximum)