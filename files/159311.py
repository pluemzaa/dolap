f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
o = input("Enter the operator(+, -, *, /):")
a = 0

if o == '+':
    a = f + s 
    print(f"Result : {a:.2f}")
elif o == '-':
    a = f - s 
    print(f"Result : {a:.2f}")
elif o == '*':
    a = f * s
    print(f"Result : {a:.2f}")       
elif o == '/':
    if f > 0 and s > 0 :
        a = f / s 
        print(f"Result : {a:.2f}") 
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")