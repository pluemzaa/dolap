number1 = input("Enter the first number: ")
num1 = int(number1)
number2 = input("Enter the second number: ")
num2 = int(number2)
sign = input("Enter the operator (+, -, *, /): ")

if sign == '+':
    result = num1 + num2
    print(f"Result : {result:.2f}")
elif sign == '-':
    result = num1 - num2
    print(f"Result : {result:.2f}")
elif sign == '*':
    result = num1 * num2
    print(f"Result : {result:.2f}")
elif sign == '/':
    if num2 == 0:
      print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"Result : {result:.2f}")
else:print("Invalid operator")