x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = input("Enter the operator (+, -, *, /): ")
if z == "+":
    re = x+y
    print(f"Result : {re:.2f}")
elif z == "-":
    re = x-y
    print(f"Result : {re:.2f}")  
elif z == "*":
    re = x*y
    print(f"Result : {re:.2f}")
if z == "/":
    if x == 0:
        print("Cannot divide by zero")
    elif y == 0:
        print("Cannot divide by zero")
    else:
        re = x/y
        print(f"Result : {re:.2f}")
else:
    print("Invalid operator")