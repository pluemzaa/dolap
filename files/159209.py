one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))
res = 0

if op == ("+") :
    res = one + two
    print ("Result : %.2f" %res)
elif op == ("-") :
    res = one - two
    print ("Result : %.2f" %res)
elif op == ("*") :
    res = one * two
    print ("Result : %.2f" %res)
elif op == ("/") :
    if two != 0 :
        res = one / two
        print ("Result : %.2f" %res)
    else :
        print ("Cannot divide by zero")
else :
    print ("Invalid operator")