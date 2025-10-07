n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op in ('+','-','*','/'):
    if op == '+' :
        print(f'Result : {n1+n2:.2f} ')
    elif op == '-' :
        print(f'Result : {n1-n2:.2f} ')
    elif op == '*' :
        print(f'Result : {n1*n2:.2f} ')
    elif op == '/' :
        if n2 !=0:
            print(f'Result : {n1/n2:.2f} ')
        else:
            print('Cannot divide by zero')
else :
    print("Invalid operator")