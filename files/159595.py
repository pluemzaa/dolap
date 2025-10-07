f = int(input("Enter the first number:"))
s = int(input("Enter the second number:"))
o = str(input("Enter the operator (+, -, *, /):"))
result = 0
if o == '+':
    result = f+s
    print(f"Result: {result:.2f}")
elif o =='-':
    result = f-s
    print(f"Result: {result:.2f}")
elif o == '*':
    result = f*s
    print(f"Result: {result:.2f}")
elif o =='/':
    if s == 0:
        print("Cannot divide by zero")
    else:
        result = f/s
        print(f"Result: {result:.2f}")
else:
    print("Invalid operator")