s = float(input("Enter the first number:"))
a = float(input("Enter the second number:"))
b = input("Enter the operator (+, -, *, /):")
c = 0
if b == '+': 
    c = s+a
    print(f"Result:{c:.2f}")
elif b=="-":
    c = s-a
    print(f"Result:{c:.2f}")
elif b=="*":
    c = s*a
    print(f"Result:{c:.2f}")
elif b=="/":
    if a==0:
        print("Cannot divide by zero")
    else :
        c = s/a
        print(f"Result:{c:.2f}")
else:
    print("Invalid operator")