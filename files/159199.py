f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
o_list = ["+", "-", "*", "/"]
if o in o_list:
    if o == o_list[0]:
        print(f"Result : {f + s:.2f}")
    elif o == o_list[1]:
        print(f"Result : {f - s:.2f}")
    elif o == o_list[2]:
        print(f"Result : {f * s:.2f}")
    elif o == o_list[3]:
        if s > 0:
            print(f"Result : {f / s:.2f}")
        else:
            print("Cannot divide by zero")  
else:
    print("Invalid operator")