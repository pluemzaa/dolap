f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
price = 0
if o == '+' or '-' or '*' or '/':
    if f and s == 0:
        print("Cannot divide by zero")
    elif o=='+':
        price = f+s
        print(f"Result : {price:.2f}")
    elif o=='-':
        price = f-s
        print(f"Result : {price:.2f}")
    elif o=='*':
        price = f*s
        print(f"Result : {price:.2f}")
    elif o=='/':
        price = f/s
        print(f"Result : {price:.2f}")
    else:
        print("Invalid operator")