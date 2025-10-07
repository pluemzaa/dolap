fn = int(input("Enter the first number: "))
sn = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /):")

if op == "+" :
    print(F"Result : {fn + sn : .2f}")
elif op == "-" :
    print(F"Result : {fn - sn : .2f}")
elif op == "*" :
    print(F"Result : {fn * sn : .2f}")
elif op == "/" :
    if sn != 0 :
        print(F"Result : {fn / sn : .2f}")
    else :
        print("Cannot divide by zero")
else :
    print("Invalid operator")