w = float(input("Enter the first number: "))
h = float(input("Enter the second number: "))
s = input("Enter the operator (+, -, *, /): ")
if s == "+" :
    n = w + h
    print(f"Result : {n:.2f}")
if s ==  "-" :
        n = w - h          
        print(f"Result : {n:.2f}")
elif s == "*" :
        n = w * h
        print(f"Result : {n:.2f}")
elif s == "/" :
    if h == 0:
                print("Cannot divide by zero")
    else:
                n = w / h
                print(f"Result : {n:.2f}")
else:
    print("Invalid operator")