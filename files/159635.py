n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
operator=input("Enter the operator (+, -, *, /):")
if operator == '+':
    print("Result :%.2f" % (n1+n2))
elif operator == '-':
    print("Result :%.2f" % (n1-n2))
elif operator == '*':
    print("Result :%.2f" % (n1*n2))
elif operator == '/':
    if n2 == 0:
        print("Cannot divide by zero")
    else:
     print("Result :%.2f" % (n1/n2))
else:
    print("Invalid operator")