n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
C = input("Enter the operator (+, -, *, /):")

if C == "+" or C == "-" or C == "*" or C == "/" :
    if C=="+":
        P = n1+n2
        print(f"Result : {P:.2f}")
    if C=="-":
        P = n1-n2
        print(f"Result : {P:.2f}")
    if C=="*":
        P = n1*n2
        print(f"Result : {P:.2f}")
    if C=="/":
        if n2 == 0:
            print("Cannot divide by zero")
        else:
            P = n1/n2
            print(f"Result : {P:.2f}")
else:
    print("Invalid operator")