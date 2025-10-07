w = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
x = input("Enter the operator (+, -, *, /):")
if x in ["+","-","*","/"]:
    if s!=0:
        if x == '+':
            result = w + s
        elif x == '-':
            result = w - s
        elif x == '*':
            result = w * s
        elif x == '/':
            result = w / s
        print(f"Result: {result:.2f}")
    else:
        print("Cannot divide by zero")
else:
        print("Invalid operator")