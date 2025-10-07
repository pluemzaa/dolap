fi = float(input("Enter the first number: "))
se = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == '+':
    re = (fi + se)
    print("Result: %.2f" % re)
elif op == '-':
    re = (fi - se)
    print("Result: %.2f" % re)
elif op == '*':
    re = (fi * se)
    print("Result: %.2f" % re)
elif op == '/':
    if se == 0:
        print("Cannot divide by zero")
    else :
        re = (fi / se)
        print("Result: %.2f" % re)
else:
    print("Invalid operator")