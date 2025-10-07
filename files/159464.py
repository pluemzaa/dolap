num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
op=input("Enter the operator (+, -, *, /):")
if op not in ['+','-','*','/']:
    print("Invalid operator")
elif op =='/'and num2==0:
    print("Cannot divide by zero")
else:
    if op =='+':
        Result= num1+num2
    elif op =='-':  
        Result= num1-num2
    elif op=='*':
        Result= num1*num2
    elif op=='/':
        Result= num1/num2
    print(f"Result:{Result:.2f}")