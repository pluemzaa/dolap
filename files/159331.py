f = float(input("Enter the first number: "))
s = float(input("Enter the second number:"))
o = (input("Enter the operator (+, -, *, /): "))
if o == "+":
    n1 = f+s
    print(f"Result :  {n1:.2f}")
elif o == "-":
    n2 = f-s
    print(f"Result :  {n2:.2f}")
elif o == "*":
    n3 = f*s
    print(f"Result :  {n3:.2f}")
elif o == "/":
    if s == 0:
        print("Cannot divide by zero")
    else:
        n4 = f/s
        print(f"Result :  {n4:.2f}")
else :
    print("Invalid operator")