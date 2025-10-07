f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
temp = 0
operators = ['+', '-', '*', '/']

if o in operators:
    if s != 0:
        if o == '+':
            temp = f + s
        elif o == '-':
            temp = f-s
        elif o == '*':
            temp = f*s 
        else:
            temp = f/s
        print(f"Result: {temp:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")