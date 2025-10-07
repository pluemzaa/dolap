first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = first+second
    print(f"Result:{result:.2f}")
elif operator == '-':
    result = first-second
    print(f"Result:{result:.2f}")
elif operator == '*':
    result = first*second
    print(f"Result:{result:.2f}")
elif operator == '/':
    if second == 0:
        print("Cannot divide by zero")
    else:
        result = first / second
        print(f"Result:{result:.2f}")
else:
    print("Invalid operator")