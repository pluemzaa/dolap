# รับ input จากผู้ใช้
input_str = input("Input: ")

# แยกค่าด้วย comma และลบช่องว่างเผื่อมีการเว้นวรรค
a_str, b_str = input_str.split(",")
a = int(a_str.strip())
b = int(b_str.strip())

# แสดงผลการคำนวณ
print(f"{a}+{b}={a + b}")
print(f"{a}-{b}={a - b}")
print(f"{a}*{b}={a * b}")
print(f"{a}/{b}={a / b}")
print(f"{a}//{b}={a // b}")
print(f"{a}%{b}={a % b}")
print(f"{a}**{b}={a ** b}")