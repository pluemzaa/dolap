f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
i = input("Enter the operator (+, -, *, /): ")

if i == "+":
    result = f + s
    print(f"Result: {result:.2f}")
elif i == "-":
    result = f - s
    print(f"Result: {result:.2f}")
elif i == "*":
    result = f * s
    print(f"Result: {result:.2f}")
elif i == "/":
    if s == 0:
        print("Cannot divide by zero")
    else:
        result = f / s
        print(f"Result: {result:.2f}")
else:
    print("Invalid operator")