f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
r = o
if o == "+":
    r = f + s
    print("Result:%.2f"% (r))
elif o == "-":
    r = f - s
    print("Result:%.2f"% (r))
elif o == "*":
    r = f * s
    print("Result:%.2f"% (r))
elif o == "/":
    if s == 0:
        print("Cannot divide by zero")
    else:
        r = f / s
        print("Result : %.2f"% (r))
    
else:
    print("Invalid operator")