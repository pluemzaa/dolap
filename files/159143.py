num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opt = input("Enter the operator (+, -, *, /):")
if opt == "+" or opt == "-" or opt == "*" or opt == "/" :
    if opt == "+" :
        Result = num1+num2
        print(f"Result : {Result:.2f}")
    elif opt == "-" :
        Result = num1-num2
        print(f"Result : {Result:.2f}")
    elif opt == "*" :
        Result = num1*num2
        print(f"Result : {Result:.2f}")
    elif opt == "/" :
        if num2 == 0:
            print("Cannot divide by zero")
        else :
            Result = num1 / num2  
            print(f"Result : {Result:.2f}")
else : 
    print("Invalid operator")