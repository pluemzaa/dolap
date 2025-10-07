# รับค่าจากผู้ใช้
input_str = input("Enter a series of numbers separated by commas: ")

# แปลง input เป็น list ของ float
numbers = list(map(float, input_str.split(',')))

# คำนวณค่า min และ max
min_val = min(numbers)
max_val = max(numbers)

# ทำ normalization
normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

# แสดงผล
print("Normalized values:")
for val in normalized:
    print(f"{val:.2f}")