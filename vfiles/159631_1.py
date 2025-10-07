# เครื่องคิดเลขแบบง่าย

# รับค่าตัวเลขจากผู้ใช้
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

# ตรวจสอบตัวดำเนินการ
if op not in ['+', '-', '*', '/']:
    print("Invalid operator")
else:
    if op == '/':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result : %.2f" % result)
    elif op == '+':
        result = num1 + num2
        print("Result : %.2f" % result)
    elif op == '-':
        result = num1 - num2
        print("Result : %.2f" % result)
    elif op == '*':
        result = num1 * num2
        print("Result : %.2f" % result)