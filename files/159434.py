f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
if o =='+':
    p = f + s
    print(f"Result :{p:.2f}")
elif o == '-':
    m = f - s
    print(f"Result :{m:.2f}")
elif o == '*':
    k = f * s
    print(f"Result :{k:.2f}")
elif o == '/':
    if s == 0:
        print("Cannot divide by zero")
    else:
        h = f / s
        print(f"Result :{h:.2f}")

else:
    print("Invalid operator")