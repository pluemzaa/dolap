w = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
f = input("Enter the operator (+, -, *, /):")
if f in ["+","-","*","/"]:
    if f== "+":
        r= w + s
        print(f"Result: {w+s:.2f}")
    if f== "-":
        r= w - s
        print(f"Result: {r:.2f}")
    if f== "*":
        r= w * s
        print(f"Result: {r:.2f}")   
    if f== "/":
        if s== 0:
            print("Cannot divide by zero")
            exit()
        else: 
            r=w/s   
            print(f"Result: {r:.2f}")
else:
    print("invalid operator")