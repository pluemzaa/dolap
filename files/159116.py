f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == "+":
    print(f"Result : {(f + s):.2f}")
elif op == "-":
    print(f"Result : {(f - s):.2f}")
elif op == "*":
    print(f"Result : {(f * s):.2f}")
elif op == "/":
    if s > 0:
        print(f"Result : {(f / s):.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")