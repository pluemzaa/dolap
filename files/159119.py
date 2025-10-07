num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

ope = input("Enter the operator (+, -, *, /): ")
if ope == "+":
        r = num1 + num2
        print(f"Result : {r:.2f}")
elif ope == "-":
        r = num1 - num2
        print(f"Result : {r:.2f}")
elif ope == "*":
        r = num1 * num2
        print(f"Result : {r:.2f}")
elif ope == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        r = num1 / num2
        print(f"Result : {r:.2f}")
else:
    print("Invalid operator")