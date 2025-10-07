f = float(input("Enter the first number: "))
s = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
r=0
p = ['+', '-', '*', '/']

if s == 0 and o== '/' :
        print("Cannot divide by zero")
else :
        if o in p : 
                if o == '+' :
                        r=f+s 
                elif o == '-' :
                        r=f-s
                elif o == '*' :
                        r=f*s
                elif o == '/' :
                        r=f/s      
                print(f"Result : {r:.2f}")  
        else :
                print("Invalid operator")