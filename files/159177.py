num = int(input("Enter the first number:"))
num1 = int(input("Enter the second number:"))
ca = str(input("Enter the operator (+, -, *, /):"))
Result=0
if ca=='+':
    Result=num+num1
    print(f"Result :{Result:.2f}")
elif ca =='-' :
    Result=num-num1
    print(f"Result :{Result:.2f}")
elif ca =='*':
    Result=num*num1
    print(f"Result :{Result:.2f}")
elif ca=='/':
    if num1== 0:
        print("Cannot divide by zero")   
    else:
        Result=num/num1
        print(f"Result :{Result:.2f}")
else:
    print("Invalid operator")