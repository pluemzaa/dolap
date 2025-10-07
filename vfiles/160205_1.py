# รับข้อมูลจากผู้ใช้
input_data = input("Enter a series of numbers separated by commas: ")
numbers = input_data.split(',')

# แปลง string เป็น int
for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

# คำนวณ min และ max
min_value = min(numbers)
max_value = max(numbers)

print("Normalized values:")

# ปรับช่วงข้อมูลให้อยู่ในช่วง [0, 1]
for num in numbers:
    if max_value == min_value:
        normalized = 0.0  # ป้องกันหาร 0 ถ้าค่าทุกตัวเท่ากัน
    else:
        normalized = (num - min_value) / (max_value - min_value)
    print("{:.2f}".format(normalized))