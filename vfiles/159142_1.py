# รับค่าตัวเลขสองจำนวน
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# รับค่าตัวดำเนินการ
operator = input("Enter the operator (+, -, *, /): ")

# ตรวจสอบตัวดำเนินการ
if operator == '+':
    result = num1 + num2
    print("Result : {:.2f}".format(result))
elif operator == '-':
    result = num1 - num2
    print("Result : {:.2f}".format(result))
elif operator == '*':
    result = num1 * num2
    print("Result : {:.2f}".format(result))
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result : {:.2f}".format(result))
else:
    print("Invalid operator")