num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")

if o == "+" or o == "-" or o == "*" or o == "/" :
    if o == "+":
        num = num1 + num2
        print(f"Result : {num:.2f}")
    elif o == "-":
        num = num1 - num2
        print(f"Result : {num:.2f}")
    elif o == "*":
        num = num1 * num2
        print(f"Result : {num:.2f}")
    elif o == "/":
        if num2 > 0:
            num=num1 / num2
            print(f"Result : {num:.2f}")
        elif num2 <= 0:
            print("Cannot divide by zero")
else:
    print("Invalid operator")