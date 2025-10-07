n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operator = str(input("Enter the operator (+, -, *, /): "))

if operator == "+":
    print(f"Result : {(n1+n2):.2f}")
elif operator == "-":
    print(f"Result : {(n1-n2):.2f}")
elif operator == "*":
    print(f"Result : {(n1*n2):.2f}")
elif operator == "/":
    if n2 != 0:
        print(f"Result : {(n1/n2):.2f}")
    else :  
        print("Cannot divide by zero")
else:
    print("Invalid operator")