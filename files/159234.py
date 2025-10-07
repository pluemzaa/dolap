a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the operator (+, -, *, /): ")

if c == "+" or c == "-" or c == "*" or c == "/":
    if b == 0 and c == "/":
        print("Cannot divide by zero")
    else:
        if c == "+":
            d = a + b
        elif c == "-":
            d = a - b
        elif c == "*":
            d = a * b
        else:
            d = a / b
        print(f"Result : {d:.2f}")
else:
    print("Invalid operator")