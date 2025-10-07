x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
o = str(input("Enter the operator (+, -, *, /): "))
r = 0
if o == "+":
    r = x + y
    print("Result : %.2f"% (r))
if o == "-":
    r = x - y
    print("Result : %.2f"% (r))
elif o == "*":
    r = x * y
    print("Result : %.2f"% (r))
elif o == "/":
    if y == 0:
        print("Cannot divide by zero")
    else:
        r = x / y
        print("Result : %.2f"% (r))
            
else:
    print(:"Invalid operator")