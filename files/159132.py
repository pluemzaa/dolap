num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))

if op == "+" or op == "-" or op == "*" or op == "/":
    if op == "+":
        Result = num1 + num2
        print(f"Result : {Result:.2f}")
    elif op == "-":
        Result = num1 - num2
        print(f"Result : {Result:.2f}")
    elif op == "*":
        Result = num1 * num2
        print(f"Result : {Result:.2f}")
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            Result = num1 / num2
            print(f"Result : {Result:.2f}")
    #print(f"Result : {Result:.2f}")
else:
    print("Invalid operator")