FN = int(input("Enter the first number:"))
SN = int(input("Enter the second number:"))
OP = input("Enter the operator (+, -, *, /):")
if OP == '+':
    PL = FN + SN
    print(f"Result: {PL:.2f}")
elif OP == '-':
    MN = FN - SN
    print(f"Result: {MN:.2f}")
elif OP == '*':
    MUL = FN * SN
    print(f"Result: {MUL:.2f}")
elif OP == "/":
    if SN > 0:
        DV = FN / SN
        print(f"Result: {DV:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")