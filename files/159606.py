num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
add = input("Enter the operator (+, -, *, /):")
if add == '+' :
    reji = num1+num2
    print("Result : ","%.2f"%reji)
elif add == '-' :
    reji = num1-num2
    print("Result : ","%.2f"%reji)
elif add == '*' :
    reji = num1*num2
    print("Result : ","%.2f"%reji)
elif add == '/' :
    if num2 == 0 :
        print("Cannot divide by zero")
    else:
     reji = num1/num2
     print("Result : ","%.2f"%reji)
else:
    print("Invalid operator")