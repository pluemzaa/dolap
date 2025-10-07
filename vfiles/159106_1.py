x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")


if op == '+':
    Result = x+y
    print(f"Result : {Result:.2f}")
elif op == '-':
    Result = x-y
    print(f"Result : {Result:.2f}")
elif op == '*':
    Result = x*y
    print(f"Result : {Result:.2f}")
elif op == '/' and y != 0:
    Result = x/y
    print(f"Result : {Result:.2f}")
elif op == '/' and y == 0:
    print("Cannot divide by zero")
else:
    print("Invalid operator")