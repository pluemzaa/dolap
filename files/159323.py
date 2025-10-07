num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))


if num1 == 0 or num2 ==0 and op == "/" :
    print ("Cannot divide by zero")
elif op == "+":
    print ("Result : %.2f" %(num1+num2))
elif op == "-":
    print ("Result : %.2f" %(num1-num2))
elif op == "*":
    print ("Result : %.2f" %(num1*num2))
elif op == "/":
    print ("Result : %.2f" %(num1/num2))
else :
    print ("Invalid operator")