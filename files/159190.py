num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /):")
sum = 0 
if op == "+" :
    sum=num1+num2
    print(f"Result : {sum:.2f}")
elif op == "-" :
    sum=num1-num2
    print(f"Result : {sum:.2f}")
elif op == "*" :
    sum=num1*num2
    print(f"Result : {sum:.2f}")
elif op == "/" :
    if num2 > 0 :
        sum=num1/num2
        print(f"Result : {sum:.2f}")
    else:
        print("Cannot devide by zero")
else :
    print("invalid operator")