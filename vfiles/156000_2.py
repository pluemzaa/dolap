# รับค่าตัวเลขจากผู้ใช้ คั่นด้วย comma
input_str = input("Enter two numbers separated by a comma: ")

# แยกและแปลงค่าเป็นจำนวนเต็ม พร้อมตัดช่องว่าง
num1_str, num2_str = input_str.split(",")
num1 = int(num1_str.strip())
num2 = int(num2_str.strip())

# แสดงผลลัพธ์
print(f"{num1}+{num2}={num1 + num2}")
print(f"{num1}-{num2}={num1 - num2}")
print(f"{num1}*{num2}={num1 * num2}")
print(f"{num1}/{num2}={num1 / num2}")
print(f"{num1}//{num2}={num1 // num2}")
print(f"{num1}%{num2}={num1 % num2}")
print(f"{num1}**{num2}={num1 ** num2}")