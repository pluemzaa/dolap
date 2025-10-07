fn=float(input("Enter the first number:"))
sn=float(input("Enter the second number:"))
op=input("Enter the operator (+, -, *, /):")
R=0
if op=='+'or'-'or'*'or'/':
    if fn and sn==0 :
            print("Cannot divide by zero")
    elif op=='+':
        R= fn+sn
        print(f"Result :{R:.2f}")
    elif op=='-':
        R= fn-sn
        print(f"Result :{R:.2f}")
    elif op=='*':
        R= fn*sn
        print(f"Result :{R:.2f}")
    elif op=='/':
            R=fn/sn
            print(f"Result :{R:.2f}")        
    else:
        print("Invalid operator")