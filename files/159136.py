first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
op = input("Enter the operator (+, -, *, /):")
result = 0

if op == '+':
        result = first + second
        print(f"Result : {result:.2f}")
elif op == '-':
        result = first - second
        print(f"Result : {result:.2f}")
elif op == '*':
        result = first * second
        print(f"Result : {result:.2f}")
elif op == '/':
    if second == 0:
        print("Cannot divide by zero")
    else:
        result = first / second
        print(f"Result : {result:.2f}")
else:
    print("Invalid operator")