f = int(input("Enter the first number"))
s = int(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
z  = 0
if o == '+':
    z = f+s
    
elif o == '-':
    z = f-s
    
elif o == '*':
    z = f*s
    
elif o == '/':
    if s == 0:
        z=0
    else:
        z=f/s
        
print(f"Result : {z:.2f}")