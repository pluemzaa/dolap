n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == "+":
    num = n1 + n2
    print(f"Result : {num:.2f}")
elif op == "-":
    num = n1 - n2
    print(f"Result : {num:.2f}")
elif op == "*":
    num = n1 * n2
    print(f"Result : {num:.2f}")
elif op == "/":
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        num = n1 / n2
        print(f"Result : {num:.2f}")
else:
    print("Invalid operator")