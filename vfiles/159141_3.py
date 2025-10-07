fn = int(input("Enter the first number:"))
sn = int(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
if sn > 0:
    if o == "+":
        x1 = fn + sn
        print(f"Result:{x1:.2f}")
    elif o == "-":
        x2 = fn - sn
        print(f"Result:{x2:.2f}")
    elif o == "*":
        x3 = fn * sn
        print(f"Result:{x3:.2f}")
    elif o == "/":
        x4 = fn / sn
        print(f"Result:{x4:.2f}")        
    else:
        print("Invalid operator")
else:
    print("Cannot divide by zero")