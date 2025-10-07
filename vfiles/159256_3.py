num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oper = input("Enter the operator (+,-,*,/): ")

oper_list = ["+","-","*","/"]

if oper not in oper_list:
    print("Invalid operator")
else:
    if oper == "/" and num2 == 0:
        print("Cannot divide by zero")
    else:
        if oper == "+":
            print(f"Result: {num1 + num2:.2f}")
        elif oper == "-":
            print(f"Result: {num1 - num2:.2f}")
        elif oper == "*":
            print(f"Result: {num1 * num2:.2f}")
        elif oper == "/":
            print(f"Result: {num1 / num2:.2f}")
✅ จุดที่แก้:
เช็กว่าเป็น / ก่อนค่อยเช็กว่า num2 == 0

ใช้ else: แทนการเช็กซ้ำ if oper in oper_list: หลังจาก if oper not in oper_list: เพื่อไม่ให้โค้ดทำงานซ้ำซ้อน

แบบนี้จะถูกต้องและปลอดภัยจากการหารด้วยศูนย์ครับ.








You said:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 == 0:
    print("Cannot divide zero")
oper = input("Enter the operator (+,-,*,/): ")

oper_list = ["+","-","*","/"]

if oper not in oper_list:
    print("Invalid operator")
    
if oper in oper_list:
    if oper == oper_list[0]:
        print(f"Result:{num1 + num2:.2f}")
    elif oper == oper_list[1]:
        print(f"Result:{num1 - num2:.2f}")
    elif oper == oper_list[2]:
        print(f"Result:{num1 * num2:.2f}")
    elif oper == oper_list[3]:
        print(f"Result:{num1 / num2:.2f}")


ChatGPT said:
โค้ดนี้ยังมีปัญหา แม้ผู้ใช้จะไม่เลือกหาร (/) ก็ยังตรวจ num2 == 0 แล้วแสดง "Cannot divide zero" ออกมา ซึ่งไม่ควรเกิด

✅ โค้ดที่แก้ไขแล้ว:
python
Copy
Edit
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oper = input("Enter the operator (+,-,*,/): ")

oper_list = ["+", "-", "*", "/"]

if oper not in oper_list:
    print("Invalid operator")
elif oper == "/" and num2 == 0:
    print("Cannot divide by zero")
else:
    if oper == "+":
        print(f"Result: {num1 + num2:.2f}")
    elif oper == "-":
        print(f"Result: {num1 - num2:.2f}")
    elif oper == "*":
        print(f"Result: {num1 * num2:.2f}")
    elif oper == "/":
        print(f"Result: {num1 / num2:.2f}")