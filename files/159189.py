n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
x = input("Enter the operator (+, -, *, /): ")
if x in ['+', '-','*', '/']:
    if n2 != 0 :   
        if x == '+':
            Result = n1 + n2
        elif x == '-':
            Result = n1 - n2
        elif x == '*':
            Result = n1 * n2
        elif x == '/':
            Result = n1 / n2
        print(f"Result : {Result:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")