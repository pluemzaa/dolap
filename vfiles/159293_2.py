fn = int(input("Enter first number:"))
sn = int(input("Enter second number:"))
op = input("Enter the operator (+, -, *, /):")
O = ["+","-","*","/"]

if op in O:
    if op == "+":
        rs = fn + sn
        print(f"Result : {rs:.2f}")
    elif op == "-":
        rs = fn - sn
        print(f"Result : {rs:.2f}")
    elif op == "*":
        rs = fn * sn
        print(f"Result : {rs:.2f}")
    elif op == "/":
        if fn > 0 and sn > 0:
            rs = fn / sn
            print(f"Result : {rs:.2f}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")