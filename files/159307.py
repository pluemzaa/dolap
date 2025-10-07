num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op1 = input("Enter the operator (+, -, *, /):")
op2 = ["+","-","*","/"]
if op1 in op2:
    if op1 == "+":
        print(f"Result : {num1+num2:.2f}")
    if op1 == "-":
        print(f"Result : {num1-num2:.2f}")
    if op1 == "*":
        print(f"Result : {num1*num2:.2f}")
    if op1 == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result : {num1/num2:.2f}")
else:
    print("Invalid operator")