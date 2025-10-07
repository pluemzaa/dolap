x =float(input("Enter the first number:"))
y =float(input("Enter the second number:"))
z =input("Enter the operator (+, -, *, /):")

if z =="+" or z =="*" or z =="-" or z =="/":
    if z == "+":
        total = x + y
        print(f"Result :{total:.2f}")
    elif z == "*":
        total = x * y
        print(f"Result : {total:.2f}")
    elif z == "-":
        total = x-y
        print(f"Result : {total:.2f}")
    elif z == "/":
        if y != 0:
            total =x/y
            print(f"Result : {total:.2f}")
        else:
            print(f"Cannot divide by zero")
else:
    print("Invalid operator")