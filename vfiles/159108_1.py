num = 0
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))
ope =input("Enter the operator (+, -, *, /): ")
if ope =="+" or ope =="-" or ope =="*" or ope =="/":
    if ope =="+":
        num = num1 + num2
        print(f"Result : {num:.2f}")   
    elif ope =="-":
        num = num1 - num2
        print(f"Result : {num:.2f}")   
    elif ope =="*":
        num = num1 * num2
        print(f"Result : {num:.2f}")   
    elif ope =="/":
        if num2==0:
            print("Cannot divide by zero")
        else:
            num = num1 / num2
            print(f"Result : {num:.2f}")   
else:
    print("Invalid operator")