# รับค่าตัวเลขจากผู้ใช้ โดยคั่นด้วย comma
input_str = input("Enter two numbers separated by a comma: ")

# แยกค่าตัวเลขออกจากกัน
num1_str, num2_str = input_str.split(",")
num1 = int(num1_str)
num2 = int(num2_str)

# แสดงผลการคำนวณแต่ละเครื่องหมาย
print(f"{num1}+{num2}={num1 + num2}")
print(f"{num1}-{num2}={num1 - num2}")
print(f"{num1}*{num2}={num1 * num2}")
print(f"{num1}/{num2}={num1 / num2}")
print(f"{num1}//{num2}={num1 // num2}")
print(f"{num1}%{num2}={num1 % num2}")
print(f"{num1}**{num2}={num1 ** num2}")