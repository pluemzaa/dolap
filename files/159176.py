x = int(input("Enter the first number: "))
xy = int(input("Enter the second number: "))
xyx = str(input("Enter the operator (+, -, *, /): "))

if xyx == "+":
    g1 = x+xy
    print(f"Result : {g1:.2f}")
elif xyx == "-":
    g2 = x-xy
    print(f"Result : {g2:.2f}")
elif xyx == "*":
    g3 = x*xy
    print(f"Result : {g3:.2f}")
elif xy == 0:
    print("Cannot divide by zero")
elif xyx == "/":
    g4 = x/xy
    print(f"Result : {g4:.2f}")
else:
    print("Invalid operator")