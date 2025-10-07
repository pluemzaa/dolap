# รับอินพุตเป็นสตริง
input_str = input("Enter a series of numbers separated by commas: ")
# แปลงเป็นลิสต์ของตัวเลข
numbers = [int(num.strip()) for num in input_str.split(',')]

# กำหนดค่าตัวแรกเป็น maximum เริ่มต้น
maximum = numbers[0]

# วนซ้ำเริ่มจากตัวที่สอง
for num in numbers[1:]:
    if num > maximum:
        maximum = num
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")