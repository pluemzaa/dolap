num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /):")

if op == "+" or op == "-" or op == "*" or op == "/":
    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/" and num2 != 0:
        result = num1/num2
    else:
        print("Cannot divide by zero")
    print(f"Result : {result:.2f}")
else:
    print("Invalid operator")