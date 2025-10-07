fn = float(input("Enter the first number: "))
sn = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == '+':
    result = fn + sn
    print(f"Result : {result:.2f}")
elif op == '-':
    result = fn - sn
    print(f"Result : {result:.2f}")
elif op == '*':
    result = fn * sn
    print(f"Result : {result:.2f}")
elif op == '/':
    if sn == 0:
        print("Cannot divide by zero")
    else:
        result = fn / sn
        print(f"Result : {result:.2f}")
else:
    print("Invalid operator")