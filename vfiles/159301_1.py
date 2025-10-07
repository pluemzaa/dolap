N1 = int(input("Enter the first number:"))
N2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == "+" :
    re = N1 + N2
    print(f"Result : {re:.2f}")
elif op == "-" :
    re = N1 - N2
    print(f"Result : {re:.2f}")
elif op == "*" :
    re = N1 * N2
    print(f"Result : {re:.2f}")
elif op == "/" :
    if N2 == 0 :
        print ("Cannot divide by zero")
    else:
        re = N1/N2
        print(f"Result : {re:.2f}")
else:
    print("Invalid operator")