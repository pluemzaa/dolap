f = int(input("Enter the first number:"))
s = int(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
if o == '+':
    R = f + s
    print(f"Result : {R:.2f}")
elif o == '-':
    R = f - s
    print(f"Result : {R:.2f}")
elif o == '*':
    R = f * s
    print(f"Result : {R:.2f}")
elif o == '/':
    if s == 0:
        print("Cannot divide by zero")
    else:
        R = f / s
        print(f"Result : {R:.2f}")
else:
    print("Invalid operator")