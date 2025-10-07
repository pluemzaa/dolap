num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == "+" :
        re = num1 + num2
        print(f"Result : {re:.2f}")
elif op == "-" :
        re = num1 - num2
        print(f"Result : {re:.2f}")
elif op == "*" :
        re = num1 * num2
        print(f"Result : {re:.2f}")
elif op == "/" :
        if num2 != 0 :
            re = num1 / num2
            print(f"Result : {re:.2f}")
        else :
            print("Cannot divide by zero")
else : 
    print("Invalid operator")