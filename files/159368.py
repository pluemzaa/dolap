f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == "+":
    print("Result : %.2f" %(f+s))
elif op == "-":
    print("Result : %.2f" %(f-s))
elif op == "*":
    print("Result : %.2f" %(f*s))
elif op == "/":
    if s == 0:
        print('Cannot divide by zero')
    else:
        print("Result : %.2f" %(f/s))
else:
    print("Invalid operator")