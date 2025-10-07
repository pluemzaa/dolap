a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = str(input("Enter the operator (+, -, *, /):"))
q = 0
if b<=0 and op is "/":
    print("Cannot divide by zero")
else:
    if c is "+":
        q = a+b
        print(f"Result:{q:.2f}")
    elif c is "-":
        q = a-b
        print(f"Result:{q:.2f}")
    elif c is "*":
        q = a*b
        print(f"Result:{q:.2f}")
    elif c is "/":
        q = a/b
        print(f"Result:{q:.2f}")
    else:
        print("Invalid operator")