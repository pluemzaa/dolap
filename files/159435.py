Fnum = int(input("Enter the first number: "))
Snum = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
re = 0
if op == "+" or op == "-" or op == "*" or op == "/":
    if op == ("+"):
        re = Fnum + Snum
        print(f"Result : {re:.2f}")
    if op == ("-"):
        re = Fnum - Snum
        print(f"Result : {re:.2f}")
    if op == ("*"):
        re = Fnum * Snum
        print(f"Result : {re:.2f}")   
    if op == ("/"):
        if Fnum == 0 or Snum ==0 :
            print("Cannot divide by zero")
        else :
            re = Fnum / Snum
            print(f"Result : {re:.2f}")
else:
    print("Invalid operator")