Kom=int(input("Enter the first number:"))
Angy=int(input("Enter the second number:"))
Sumet=input("Enter the operator (+, -, *, /):")

if Sumet=="+":
    gee=Kom+Angy
    print(f"{gee:.2f}")
elif Sumet=="-":
    gee=Kom-Angy
    print(f"{gee:.2f}")
elif Sumet=="*":
    gee=Kom*Angy
    print(f"{gee:.2f}") 
elif Sumet=="/":
    if Angy=="0":
        print("Cannot divide by zero")
    else:
        fee=Kom/Angy
        print(f"{fee:.2f}")