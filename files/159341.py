a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the operator (+, -, *, /): ")


if c == '+':
    result = a + b
    print(f"Result : {result:.2f}")
elif c == '-':
    result = a - b
    print(f"Result : {result:.2f}")
elif c == '*':
    result = a * b
    print(f"Result : {result:.2f}")
elif c == '/':
    if b == 0:
        print("Cannot divide by zero")
    else:
        result = a / b
        print(f"Result : {result:.2f}")
else:
    print("Invalid operator")