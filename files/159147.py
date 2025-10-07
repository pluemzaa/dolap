fn = float(input("Enter the first number:"))
sn = float(input("Enter the second number:"))
op = (input("Enter the operator (+, -, *, /):"))
if op == "+":
    r = fn + sn 
    print(f"Result :{r:.2f}")
elif op == "-":
    r = fn - sn 
    print(f"Result :{r:.2f}")
elif op == "*":
    r = fn * sn
    print(f"Result :{r:.2f}")
elif op == "/":
    if sn != 0:
        r = fn / sn
        print(f"Result :{r:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")