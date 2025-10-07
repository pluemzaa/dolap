# รับ input
input_str = input("Input: ")

# แยกค่าตัวเลข
a_str, b_str = input_str.split(",")
a = int(a_str.strip())
b = int(b_str.strip())

# คำนวณและแสดงผล
print(f"{a}+{b}={a + b}")
print(f"{a}-{b}={a - b}")
print(f"{a}*{b}={a * b}")
print(f"{a}/{b}={a / b}")
print(f"{a}//{b}={a // b}")
print(f"{a}%{b}={a % b}")
print(f"{a}**{b}={a ** b}")