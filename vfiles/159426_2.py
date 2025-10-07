FN = float(input("Enter the first number:"))
LN = float(input("Enter the second number:"))
OP = input("Enter the operator (+, -, *, /):")

if '+' == OP:
    print(f"Result :{FN + LN: .2f}")
elif '-' == OP:
    print(f"Result :{FN - LN: .2f}")
elif '*' == OP:
    print(f"Result :{FN * LN: .2f}")
elif '/' == OP:
    print(f"Result :{FN / LN: .2f}")
    if FN = 0:
        print("Cannot divide by zero")
else:
    print("Invalid operator")