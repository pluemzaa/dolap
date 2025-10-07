num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oper = input("Enter the operator (+, -, *, /): ")
result = 0

if oper == "/" and num2 == 0:
    print("Cannot divide by zero")
else:
    if oper == '+':
        result = num1+num2
        print(f"Result : {result:.2f}")
    elif oper == '-':
        result = num1-num2
        print(f"Result : {result:.2f}")
    elif oper == '*':
        result = num1*num2
        print(f"Result : {result:.2f}")
    elif oper == '/':
        result = num1/num2
        print(f"Result : {result:.2f}")
    else:
        print("Invalid operator")