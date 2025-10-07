number1 = input("Enter the first number:")
num1 = int(number1)
number2 = input("Enter the second number:")
num2 = int(number2)
sign = input("Enter the operator (+, -, *, /):")
if sign == '+':
    print("Result:" + str(num1 -num2))
elif sign == '-':
    print("Result:" + str(num1 -num2))
elif sign == '/':
    print("Result:" + str(num1 /num2))
elif sign == '*':
    print("Result:" + str(num1 *num2))