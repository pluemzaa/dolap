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