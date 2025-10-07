x = input("กรอกเลขและตัวดำเนินการ (เช่น 5,+,3): ").split(",")

a = int(x[0])
op = x[1]
b = int(x[2])

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
elif op == "//":
    result = a // b
elif op == "%":
    result = a % b
elif op == "**":
    result = a ** b
else:
    result = "ตัวดำเนินการไม่ถูกต้อง"

print("ผลลัพธ์คือ:", result)