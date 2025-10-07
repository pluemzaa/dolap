first = float(input("Enter your first number:"))
second = float(input("Enter your second number:"))
op = input("Enter the operator(+, -, *, /):")
if op == "+":
    print(f"Result : {first+second:.2f}")
elif op == "-":
    print(f"Result : {first-second:.2f}")
elif op == "*":
    print(f"Result : {first*second:.2f}")
elif op == "/":
    if second > 0:
        print(f"Result : {first/second: .2f}")
    else :
        print("Cannot divide by zero")
else:    
    print("Invalid operator")