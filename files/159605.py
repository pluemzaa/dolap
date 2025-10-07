q = int(input("Enter the first number: "))
w = int(input("Enter the second number: "))
e = input("Enter the operator (+, -, *, /): ")

if e == '+':
    a = q + w
    print(f"Result: {a:.2f}")
elif e == '-':
    a = q - w
    print(f"Result: {a:.2f}")
elif e == '*':
    a = q * w
    print(f"Result: {a:.2f}")
elif e == '/':
    if w == 0:
        print("Cannot divide by zero")
    else:
        a = q / w
        print(f"Result: {a:.2f}")
else:
    print("Invalid operator")