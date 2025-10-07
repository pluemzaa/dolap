try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
        print(f"Result : {result:.2f}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result : {result:.2f}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result : {result:.2f}")
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"Result : {result:.2f}")
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input. Please enter valid numbers.")