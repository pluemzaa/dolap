f = float(input('Enter the first number:'))
s = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")

if o in ["+","-","*","/"]:
    if o == "+":
        r = f+s
        print(f"Result: {r:.2f} ")
    if o == "-":
        r = f-s
        print(f"Result: {r:.2f} ")
    if o == "*":
        r = f*s
        print(f"Result: {r:.2f} ")
    if o == "/":
        r = f+s
        if s == 0:
            print("Cannot divide by zero")
            exit()
        else:
            r = f/s
            print(f"Result: {r:.2f} ")
else:
    print("Invalid operator")