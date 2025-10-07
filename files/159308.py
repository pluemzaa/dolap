fn = float(input("Enter the first number: "))
sn = float(input("Enter the second number: "))
op = (input("Enter the operator (+, -, *, /): "))
Top = ["+","-","*","/"]
if op in Top:    
    if op == "+":
        print(f"Result : {fn+sn:.2f}")
    if op == "-":
        print(f"Result : {fn-sn:.2f}")
    if op == "*":
        print(f"Result : {fn*sn:.2f}")    
    if op == "/":
        if sn == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result : {fn/sn:.2f}")
else:
    print("Invalid operator")