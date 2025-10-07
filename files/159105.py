x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))

z = str(input("Enter the operator (+, -, *, /):")) 

if z == "+" : 
    sum = x + y
elif z == "-" :
    sum = x - y
elif z == "*" :
    sum = x * y
elif z == "/" :
    if y == 0 :
        print("Cannot divide by zero") 
    else :
        sum = x / y 
else :
    print("Invalid operator")

print(f"Result :{sum:.2f}")