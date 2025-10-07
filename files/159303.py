f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))

if op == '+' or op == '-' or op == '*' or op == '/':
    if op == '+':
        print(f"Result : {f+s:.2f}")
    if op == '-':
        print(f"Result : {f-s:.2f}")
    if op == '*':
        print(f"Result : {f*s:.2f}")
    if op == '/':
        if s == 0:
           print("Cannot divide by zero")
        else:
            print(f"Result : {f/s:.2f}")
else:
    print("Invalid operator")