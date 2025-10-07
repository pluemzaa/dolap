w = int(input("Enter the first number:"))
s = int(input("Enter the second number:"))
n = str(input("Enter the operator (+, -, *, /):"))
a = 0

if s<=0 and n is "/" :
    print("Cannot divide by zero")
    
else:
    if n is "+":
        a = w+s
        print(f"Result :{a:.2f}")
    elif n is "-":
        a = w-s
        print(f"Result :{a:.2f}")
    elif n is "*":
        a = w*s
        print(f"Result :{a:.2f}")
    elif n is "/":
        a = w/s
        print(f"Result :{a:.2f}")
    else:
        print("Invalid operator")
    
# '+'
# 1 '+' 1 

# n == "+"
#     1 + 1