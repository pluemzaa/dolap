num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
a = num1+num2
b = num1-num2
c = num1*num2
if op=="+":
    print(f"Result : {a:.2f}")
elif op=="-":
    print(f"Result : {b:.2f}")
elif op=="*":
    print(f"Result : {c:.2f}")
elif op=="/":
    if num2==0:
        print("Cannot divide by zero")
    else:
        d = num1/num2
        print(f"Result : {d:.2f}")
else:
    print("Invalid operator")