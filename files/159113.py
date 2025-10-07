first = int(input("Enter the first number: "))
secound = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator =='+':
    a = first+secound 
    print(f"Result : {a:.2f}")
elif operator =='-':
    b = first-secound
    print(f"Result : {b:.2f}")
elif operator =='*':
    c = first*secound
    print(f"Result : {c:.2f}")
elif operator =='/' and secound == 0:
    print("Cannot divide by zero")
elif operator =='/':
    d = first/secound
    print(f"Result : {d:.2f}")
else:
    print("Invalid operator")