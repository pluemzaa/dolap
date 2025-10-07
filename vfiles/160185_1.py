# รับตัวเลขจากผู้ใช้
input_numbers = input("Enter a series of numbers separated by commas: ")
numbers = input_numbers.split(',')

# แปลงค่าจาก string เป็นจำนวนเต็ม
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# ตั้งค่าตัวแรกเป็นค่า maximum เริ่มต้น
maximum = numbers[0]

# วนลูปเริ่มจากตัวที่สอง
for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        print("set the maximum value to", maximum)

# แสดงค่าสูงสุดสุดท้าย
print("The maximum value is", maximum)