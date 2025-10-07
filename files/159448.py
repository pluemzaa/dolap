num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op  in ["+", "-", "*", "/"]:
    if op == "+":
        result = num1 + num2
        print(f"Result : {result:.2f}")
    elif op == "-": 
        result = num1 - num2
        print(f"Result : {result:.2f}")
    elif op == "*":
        result = num1 * num2
        print(f"Result : {result:.2f}")
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            exit()
        else:
            result = num1 / num2
            print(f"Result : {result:.2f}")
else:
    print("Invalid operator")