f = int( input("Enter the first number: "))
s = int(input("Enter the second number: "))
p = str(input("Enter the operator (+, -, *, /): "))
if s == 0:
  print("Cannot divide by zero")
elif p == "+":
    Result = f+s
    print(f"Reasult : {Result:.2f}")
elif p == "-":
      Result = f-s
      print(f"Reasult : {Result:.2f}")
elif p == "*":
      Result = f*s
      print(f"Reasult : {Result:.2f}")
elif p == "/":
      Result = f/s
      print(f"Reasult : {Result:.2f}")
else:
  ("Invalid operator")