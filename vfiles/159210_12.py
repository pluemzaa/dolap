w = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
t = (input("Enter the operator(+, -, *, /):"))
if t== "+" :
    x = w+s
    print(f"Result :{x:.2f}")
elif t == '-':
    x = w-s
    print(f"Result :{x:.2f}")
elif t == '*':
    x = w*s
    print(f"Result :{x:.2f}")
elif t == '/':
    if s != 0:
        x = w/s
        print(f"Result :{x:.2f}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")