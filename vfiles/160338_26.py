# รับค่าจำนวนเต็มแยกด้วย comma
input_numbers = input("Enter numbers separated by commas: ")
numbers = input_numbers.split(",")  # แยกเป็นรายการ string
numbers = [int(n.strip()) for n in numbers]  # แปลงเป็น int และลบช่องว่าง

# รับค่าที่ต้องการค้นหา
target = int(input("Enter number to search: "))

# ค้นหาและแสดงผล
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        found = True

if not found:
    print(f"No {target} found")