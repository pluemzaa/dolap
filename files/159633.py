n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == '+' :
    print("Result:%.2f" % (n1 + n2))
elif op == "-" :
    print("Result:%.2f" % (n1 - n2))
elif op == "*" :
    print("Result:%.2f" % (n1 * n2))
elif op == "/" :
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:%.2f" % (n1 / n2))
else:
    print("Invalid operator")