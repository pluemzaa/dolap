n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+" or operator == "-" or operator == "*" or operator == "/" :
    if operator == "+" :
        s = n1+n2
        print(f"Result : {s:.2f}")
    if operator == "-" :
        s = n1-n2
        print(f"Result : {s:.2f}")
    if operator == "*" :
        s = n1*n2
        print(f"Result : {s:.2f}")
    if operator == "/" :
        if n2 == 0:
            print("Cannot divide by zero")
        else:
            s = n1/n2
            print(f"Result : {s:.2f}")
else:
    print("Invalid operator")