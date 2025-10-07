x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = input("Enter the operator (+, -, *, /): ")


if z not in ['+', '-', '*', '/']:
    print("Invalid operator")
elif z == '/' and y == 0:
    print("Cannot divide by zero")
    
else:     
    if z =='+':
        Result= x+y    
    elif z =='-':
        Result= x-y
    elif z == '*': 
        Result= x*y       
    elif z =='/': 
        Result: x/y
    print(f"Result: {Result:.2f}")