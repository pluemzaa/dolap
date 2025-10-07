f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
o = str(input("Enter the operator (+, -, *, /):"))
if o == "+":
    result = float(f + s)
    print(f"Result : {result:.2f}")
elif o == "-":
    result = float(f - s)
    print(f"Result : {result:.2f}")
elif o == "*":
    result = float(f * s)
    print(f"Result : {result:.2f}")
elif o == "/":
    if s == 0:
        print("Cannot divide by zero")
    else:
        result = float(f / s)
        print(f"Result : {result:.2f}")
else:
    print("Invalid operator")