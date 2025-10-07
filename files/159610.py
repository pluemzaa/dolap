f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
oper = input("Enter the operator (+, -, *, /): ")

if oper == '+':
    re = f + s
    print(f"Result : {re:.2f}")
elif oper == '-':
    re = f - s
    print(f"Result : {re:.2f}")
elif oper == '*':
    re = f * s
    print(f"Result : {re:.2f}")
elif oper == '/':
    if s== 0:
        print("Cannot divide by zero")
    else:
        re = f / s
        print(f"Result : {re:.2f}")
else :
    print("Invalid operator")