w = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
t = input("Enter the operator (+, -, *, /): ")
if t == '+':
    result = w + s
    print("Result : {:.2f}".format(result))
elif t == '-':
    result = w - s
    print("Result : {:.2f}".format(result))
elif t== '*':
 
    result = w * s
    print("Result : {:.2f}".format(result))
elif t == '/':
    if s==0:
        print("Cannot divide by zero")
    else:
        result = w / s
        print("Result : {:.2f}".format(result))
else:
    print("Invalid operator")