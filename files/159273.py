num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

op = input("Enter the operator(+,-,*,/):")
if op =="+":
    r= num1 + num2
    print(f"Result : {r:.2f}")
elif op =="-":
    r= num1 - num2
    print(f"Result : {r:.2f}")
elif op =="*":
    r= num1 * num2
    print(f"Result : {r:.2f}")
elif op == "/":
    if num1 == 0 or num2 == 0:
        print("Cannot divide by zero")
    else:
        r = num1 / num2
        print(f"Result : {r:.2f}")
else:
    print("Invalid operator")