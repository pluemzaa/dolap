a = int(input('Enter a series of numbers separated by commas:'))
b = max(a)
print(a'is the maximum value:'

# รับค่าจากผู้ใช้ คั่นด้วย comma แล้วแปลงเป็น list ของตัวเลข
numbers = input("Enter a series of numbers separated by commas: ").split(",")
numbers = [float(x) for x in numbers]

# หา maximum
maximum = max(numbers)

# แสดงผลลัพธ์ (ใช้ Comparison operators และ Logical operators)
print(f"{numbers[0]} is the maximum value:", numbers[0] == maximum)
print(f"{numbers[1]} is the maximum value:", numbers[1] == maximum)
print(f"{numbers[2]} is the maximum value:", numbers[2] == maximum)
print(f"{numbers[3]} is the maximum value:", numbers[3] == maximum)
print(f"{numbers[4]} is the maximum value:", numbers[4] == maximum)