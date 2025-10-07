# รับ input
input_str = input("Input: ")

# แยกค่าตัวเลข และลบช่องว่าง
a_str, b_str = input_str.split(",")
a = int(a_str.strip())
b = int(b_str.strip())

# แสดงผลลัพธ์ตามลำดับและรูปแบบที่ถูกต้อง
print(f"{a}+{b}={a + b}")
print(f"{a}-{b}={a - b}")
print(f"{a}*{b}={a * b}")
print(f"{a}/{b}={a / b}")
print(f"{a}//{b}={a // b}")
print(f"{a}%{b}={a % b}")
print(f"{a}**{b}={a ** b}")