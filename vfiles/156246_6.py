# รับค่าตัวเลขที่คั่นด้วย comma
input_str = input("Input (เช่น 1,2): ")

# แยกค่าที่รับเข้ามา
num1_str, num2_str = input_str.split(",")
num1 = int(num1_str)
num2 = int(num2_str)

# คำนวณและแสดงผลลัพธ์
print(f"{num1}+{num2}={num1 + num2}")
print(f"{num1}-{num2}={num1 - num2}")
print(f"{num1}*{num2}={num1 * num2}")
print(f"{num1}/{num2}={num1 / num2}")
print(f"{num1}//{num2}={num1 // num2}")
print(f"{num1}%{num2}={num1 % num2}")
print(f"{num1}**{num2}={num1 ** num2}")