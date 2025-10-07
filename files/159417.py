n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = input("Enter the operator (+, -, *, /): ")

if n3 == "+" :
    R = n1 + n2
    print(f"Result : {R:.2f}")
elif n3 == "-" :
    R = n1 - n2
    print(f"Result : {R:.2f}")
elif n3 == "*" :
    R = n1 * n2
    print(f"Result : {R:.2f}")
elif n3 == "/" :
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        R = n1 / n2
        print(f"Result : {R:.2f}")
else:
    print("Invalid operator")