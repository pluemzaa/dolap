f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
op = input("Enter the operator (+, -, *, /):")
re = 0
if op == '+':
    re = f + s
    print(f"Result : {re:.2f}")
elif op == '-':
    re = f - s
    print(f"Result : {re:.2f}")
elif op == '*':
    re = f * s
    print(f"Result : {re:.2f}")
elif op == '/':
    if s == 0:
        print("Cannot divide by zero")
    else:
        re = f / s
        print(f"Result : {re:.2f}")

else:
    print("Invalid operator")