n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = (input("Enter the operator (+, -, *, /): "))
if op == "+" or op == "-" or op == "*" or op == "/":
    if op == "+":
        a = (n1+n2)
        print("Result:%.2f"% a)
    if op == "-":
        b = (n1-n2)
        print("Result:%.2f"% b)
    if op == "*":
        c = (n1*n2)
        print("Result:%.2f"% c)
    if op == "/":
        if n2 == 0:
            print("Cannot divide by zero")
        else:
            d = (n1/n2)
            print("Result:%.2f"% d)
else:
    print("Invalid operator")