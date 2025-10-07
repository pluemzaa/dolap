# Enter the first number: 10
# Enter the second number: 30
# Enter the operator (+, -, *, /): *
# Result : 300.00

# Enter the first number: 10
# Enter the second number: 30
# Enter the operator (+, -, *, /): //
# Invalid operator

# Invalid operator
# Cannot divide by zero

f_n = float(input("Enter the first number: "))
s_n = float(input("Enter the second number: "))
ope = input("Enter the operator (+, -, *, /): ")

if(ope in ['+','-','*','/']):
    if ope == '/' and s_n == 0:
        print("Cannot divide by zero")
    elif ope == '/':
        print(f"Result : {(f_n/s_n):.2f}")
    elif ope == '+':
        print(f"Result : {(f_n+s_n):.2f}")
    elif ope == '-':
        print(f"Result : {(f_n-s_n):.2f}")
    else:
        print(f"Result : {(f_n*s_n):.2f}")
else:
    print("Invalid operator")