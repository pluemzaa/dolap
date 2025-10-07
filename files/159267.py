fn=float(input("Enter the first number: "))
sn=float(input("Enter the second number: "))
op=input("Enter the operator (+, -, *, /): ")
if op=="+"or op =="-"or op=="*"or op=="/":
    if op=="+":
        x1=fn + sn
        print(f"Result : {x1:.2f}")
    elif op=="-":
        x2=fn-sn
        print(f"Result : {x2:.2f}")
    elif op=="*":
        x3=fn*sn
        print(f"Result : {x3:.2f}")
    else:
        if sn==0:
            print("Cannot divide by zero")
        else:
            x4=fn/sn
            print(f"Result : {x4:.2f}")
else:
    print("Invalid operator")