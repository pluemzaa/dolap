f1 = float(input("Enter the first number: "))
s2 = float(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))
if op == '+' or op == '-' or op == '*' or op == '/':
    if op == '+':
        print(f"Result : {f1+s2:.2f}")
    if op == '-':
        print(f"Result : {f1-s2:.2f}")
    if op == '*':
        print(f"Result : {f1*s2:.2f}")
    if op == '/':
        if s2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result : {f1/s2:.2f}")
else:
    print("Invalid operator")