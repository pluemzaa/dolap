f = int(input("Enter the first number: "))
e = int(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")

if o in ["+", "-", "*", "/"]:
    if e != 0:
        if o == "+":
            result = f + e
        elif o == "-":
            result = f - e
        elif o == "*":
            result = f * e
        elif o == "/":
            result = f / e
        print(f"Result: {result:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")