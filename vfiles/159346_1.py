f = int(input("Enter the first number: "))
s = int(input("Enter the first number: "))
p = input("Enter the operator: ")
if s == 0:
    print("Cannot divide by zero")
if p == "+":
    Result = f+s
    print(f"Result : {Result:.2f}")
elif p == "-":
    Result = f-s
    print(f"Result : {Result:.2f}")
elif p == "*":
    Result = f*s
    print(f"Result : {Result:.2f}")
elif p == "/":
    Result = f/s
    print(f"Result : {Result:.2f}")       
else:
    print('Invalid operator')