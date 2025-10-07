f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))
result = 0
#print("Result : ", end="" , flush=True)
if op == "+" :
    result = f+s
    print(f"Result: {result:.2f}" ) 
elif op == "-":
    result = f-s
    print(f"Result: {result:.2f}" ) 
elif op == "*":
    result = f*s
    print(f"Result: {result:.2f}" ) 
elif op == "/" :
    if s == 0 :
        print("Cannot divide by zero")
    else:
        result = f/s
        print(f"Result: {result:.2f}" ) 
else:
    print("Invalid operator")