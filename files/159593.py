n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
z = 0
if o == '+':
    z = n1 + n2
    print(f"Result : {z:.2f}")
elif o == '-':
    z = n1 - n2
    print(f"Result : {z:.2f}")
elif o == '*':
    z = n1 * n2
    print(f"Result : {z:.2f}")
elif o == '/':
    if n2 == 0:
       print("Cannot divide by zero") 
    else:
       z = n1 / n2
       print(f"Result : {z:.2f}")
else:
    print("Invalid operator")