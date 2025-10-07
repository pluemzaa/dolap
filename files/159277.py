m = float(input("Enter the first number: "))
k = float(input("Enter the second number: "))
s = input("Enter the operator (+, -, *, /):")
a = "+"
b ="-"
c ="*"
d ="/"
if s == a or s == b or s == c or s == d:
    if s == a:
        r=m+k
        print(f"Result : {r:.2f}")
    if s == b:
        r=m-k
        print(f"Result : {r:.2f}")
    if s == c:
         r=m*k
         print(f"Result : {r:.2f}")
    if s == d:
        if m > 0 and k > 0:
            r=m/k
            print(f"Result : {r:.2f}")   
        else:
            print("Cannot divide by zero") 
        
else:
    print("Invalid operator")