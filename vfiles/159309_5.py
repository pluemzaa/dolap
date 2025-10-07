f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
op = input("Enter the operator (+, -, *, ,/):")

if s != 0 :
    if op == "+" or "-" or "*" or "/":
        if op == "+":
            result = f + s
            print(f"Result : {result:.2f}")
        elif op == "-":
            result = f - s
            print(f"Result : {result:.2f}")
        elif op == "*":
            result = f * s
            print(f"Result : {result:.2f}")
        elif op == "/":
            result = f / s
            print(f"Result : {result:.2f}")
        else :
            print("Invalid operator")
if s == 0:
    print ("Cannot divide by zero")