n = float(input("Enter the first number: "))
n1 = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
f = ['+', '-', '*', '/']
if o in f:
    if o is '+':
        Re = n + n1
        print(f"Result :{Re:.2f}") 
    elif o is '-':
        Re = n - n1
        print(f"Result :{Re:.2f}")  
    elif o is '*':
        Re = n * n1
        print(f"Result :{Re:.2f}") 
    elif o is '/':
        if n1 == 0:
            print("Cannot divide by zero")
        else:
             Re = n / n1
             print(f"Result :{Re:.2f}")    
           
else:
    print("Invalid operator")