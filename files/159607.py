num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
op=input("Enter the operator (+, -, *, /): ")
if num1==0 or num2==0 :
    print("Cannot divide by zero")
else:
    if op=="+":
        ans=num1+num2
        print(f"Result : {ans:.2f}")
    elif op=="-":
        ans=num1-num2
        print(f"Result : {ans:.2f}")
    elif op=="*":
        ans=num1*num2
        print(f"Result : {ans:.2f}")
    elif op=="/":
        ans=num1/num2
        print(f"Result : {ans:.2f}")
    else :
        print("Invalid operator")