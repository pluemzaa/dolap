FN = float(input("Enter the first number:"))
LN = float(input("Enter the second  number:"))
op = input("Enter the  operator (+, -, *, /):")

if    '+'== op:
     print(f"Result :{FN + LN: .2f}")
elif  '-'== op:
     print(f"Result :{FN - LN: .2f}")
elif  '*'== op:
     print(f"Result :{FN * LN: .2f}")   
elif  '/'== op:
    if LN ==0:
        print("Cannot divide by zero")
    else:
        print(f"Result :{FN / LN: .2f}")
else:
    print("Invalid operator")