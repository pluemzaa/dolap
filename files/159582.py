f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
if o == '+' or o == '-' or o == '*' or o == '/' :
    if o == '+' :
        print(f"Result :{f+s:.2f}")
    elif o == '-' :
        print(f"Result :{f-s:.2f}")
    elif o == '*' :
        print(f"Result :{f*s:.2f}")
    elif o == '/' :
        if s == 0 :
            print("Cannot divide by zero")
        else :
            print(f"Result :{f/s:.2f}")
else :
    print("Invalid operator")