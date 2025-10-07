f = float(input("Enter the first number:"))
s = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
z = 0
if o == '+':
  z = f + s
  print(f"Result : {z:.2f}")
elif o == '-':
  z = f - s
  print(f"Result : {z:.2f}")
elif o == '*'
  z = f * s
  print(f"Result : {z:.2f}")
elif o = '/'
    if s == 0:
        print("Cannot divide by zero")
    else:
        z = f / s
        print(f"Result : {z:.2f})

 else:
      print("Invalid operator")