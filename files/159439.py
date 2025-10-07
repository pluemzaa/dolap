num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = input("Enter the operator (+, -, *, /):")
if num3 == '+':
    re = (num1 + num2)
    print(f"Result : {re:.2f}")
elif num3 == '-':
    re = (num1 - num2)
    print(f"Result : {re:.2f}")
elif num3 == '*':
    re = (num1 * num2)
    print(f"Result : {re:.2f}")
elif num3 == '/' :
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        re = (num1 / num2)
        print(f"Result : {re:.2f}")
else:
    print("Invalid operator")