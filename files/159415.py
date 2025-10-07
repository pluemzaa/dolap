num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = (input("Enter the operator (+, -, *, /): "))


    
if operator == "+":
    addition = num1 + num2
    print(f"Result: {addition:.2f}")
elif operator == "-":
    subtract = num1 - num2
    print(f"Result: {subtract:.2f}")
elif operator == "*":
    multiply = num1 * num2
    print(f"Result: {multiply:.2f}")
elif num2 == 0 and operator == "/":
    print("Cannot divide by zero")
elif operator == "/":
    division = num1 / num2
    print(f"Result: {division:.2f}")
else:
    print("Invalid operator")