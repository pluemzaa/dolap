a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the operator (+, -, *, /):")

if c =='+':
    print(f"Result : {a+b:.2f}")
elif c=='-':
    print(f"Result : {a-b:.2f}")
elif c=='*':
    print(f"Result : {a*b:.2f}")
elif c=='/':
    if a==0 or b==0:
        print("Cannot divide by zero")
    else:
        print(f"Result : {a/b:.2f}")
        
else:
    print("Invalid operator")