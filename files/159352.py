y=int(input("Enter the first number: "))
z=int(input("Enter the second number: "))
q=(input("Enter the operator (+, -, *, /): "))
  
if q=="+":
    O=y+z
    print(f"Result : {O:.2f}")
elif q=="-":
    O=y-z
    print(f"Result : {O:.2f}")
elif q=="*":
    O=y*z
    print(f"Result : {O:.2f}")
elif q=="/":
    if z==0:
        print("Cannot divide by zero")
    else:
        O=y/z 
        print(f"Result : {O:.2f}")
else :
    print("Invalid operator")