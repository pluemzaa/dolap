f1 = float(input("Enter the first number: "))
f2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == '+' or op == '*' or op == '-' or op == '/':
    if op == '+':
        total = f1 + f2
        print(f"Result : {total:.2f}")
    elif op == '*':
        total = f1 * f2
        print(f"Result : {total:.2f}")
    elif op == '-':
        total = f1 - f2
        print(f"Result : {total:.2f}")
    elif op == '/':
        if f2 != 0:
            total = f1 / f2
            print(f"Result : {total:.2f}")
        else:
            print("Cannot divide by zero")
else:
    print("Invalid operator")