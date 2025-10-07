fn = int(input("Enter first number:"))
sn = int(input("Enter second number:"))
op = input("Enter the operator (+, -, *, /):")
O = ["+","-","*","/"]

if fn >= 0 and sn >= 0:
    if op in O:
        if op is "+":
            rs = fn + sn
            print(f"Result : {rs:.2f}")
        elif op is "-":
            rs = fn - sn
            print(f"Result : {rs:.2f}")
        elif op is "*":
            rs = fn * sn
            print(f"Result : {rs:.2f}")
        elif op is "/":
            if fn > 0 and sn > 0:
                rs = fn / sn
                print(f"Result : {rs:.2f}")
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid operator")