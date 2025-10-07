# รับข้อมูลจากผู้ใช้
numbers = input("Enter a series of numbers separated by commas: ")

# แปลงเป็น list ของตัวเลข
num_list = [int(n) for n in numbers.split(",")]

# หาค่าสูงสุด
maximum = max(num_list)

# ตรวจสอบและแสดงผลลัพธ์
[print(f"{n} is the maximum value: {(n == maximum) and True or False}") for n in num_list]