n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
a = n1+n2
b = n1-n2
c = n1*n2
if op=="+":
    print(f"Result : {a:.2f}")
elif op=="-":
    print(f"Result : {b:.2f}")
elif op=="*":
    print(f"Result : {c:.2f}")
elif op=="/":
    if n2==0:
        print("Cannot divide by zero")
    else:
        d = n1/n2
        print(f"Result : {d:.2f}")
else:
    print("Invalid operator")