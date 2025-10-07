n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /):")

if op == "+" or op == "-" or op == "*" or op == "/" :
    if op=="+":
        P = n1+n2
        print(f"Result : {P:.2f}")
    if op=="-":
        P = n1-n2
        print(f"Result : {P:.2f}")
    if op=="*":
        P = n1*n2
        print(f"Result : {P:.2f}")
    if op=="/":
        if n2 == 0:
            print("Cannot divide by zero")
        else:
            P = n1/n2
            print(f"Result : {P:.2f}")
else:
    print("Invalid operator")