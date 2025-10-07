num1 = float(input("Enter the first number:"))      
num2 = float(input("Enter the second number:"))
oper = input("Enter the operator (+, -, *, /):")     
if oper == '+':
    print("Result: %.2f" % (num1 + num2))
elif oper == '-':
    print("Result: %.2f" % (num1 - num2))
elif oper == '*':
    print("Result: %.2f" % (num1 * num2))
elif oper == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result: %.2f" % (num1 / num2))
else:
    print("Invalid operator")