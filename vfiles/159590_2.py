n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = (input("Enter the operator (+, -, *, /): "))

if op =='+':
    out = n1 + n2
    print(f"Result : {out:.2f}")
elif op =='-':
    out = n1 - n2
    print(f"Result : {out:.2f}")
elif op =='*':
    out = n1 * n2
    print(f"Result : {out:.2f}")
elif op =='/':
    out = n1 / n2
    print(f"Result : {out:.2f}")
else:
    print("Invalid operator")
#print(f"Result : {out:.2f}")