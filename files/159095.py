x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
o = input("Enter the operator (+, -, *, /): ")
olist = ["+","-","*","/"]
if o not in olist :
    print("Invalid operator")
elif y == 0 :
    print("Cannot divide by zero")
else :
    if o == "+":
      sum = x+y
    elif o == "-":
          sum = x-y
    elif o == "*":
          sum = x*y
    elif o == "/":
          sum = x/y
    print(f"Result : {sum:.2f}")