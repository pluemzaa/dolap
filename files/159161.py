n = int(input("Enter the first number: "))
f = int(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
if o in ["+","-","*","/"]:
    if f != 0:
        if o == "+":
            Result = n + f
        elif o == "-":
            Result = n - f
        elif o == "*":
            Result = n * f
        elif o == "/":
            Result = n / f
        print(f"Result : {Result:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")