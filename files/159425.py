a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = input("Enter the operator (+, -, *, /):")



if c == "+":
    print("Result :%.2f"  %(a + b))
elif c == "-":
    print("Result :%.2f" % (a - b))
elif c == "*":
    print("Result :%.2f" % (a*b))
elif c == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result :%.2f" % (a / b))
else:
    print("Invalid operator")