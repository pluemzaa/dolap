F = float(input("Enter the first number: "))
S = float(input("Enter the second number: "))
O = input("Enter the operator (+, -, *, /): ")
if O =='+':
    re = (F+S)
    print(f"Result :{re:.2f}")
elif O =='-':
    re = (F-S)
    print(f"Result :{re:.2f}")
elif O =='*':
    re = (F*S)
    print(f"Result :{re:.2f}")
elif O =='/':
    if S == 0:
        print("Cannot divide by zero")
    else:
        re = (F/S)
        print(f"Result :{re:.2f}")
else:
    print("Invalid operator")