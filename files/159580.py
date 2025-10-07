n = float(input("Enter the first number:"))
t = float(input("Enter the second number:"))
o = input("Enter the operator (+, -, *, /):")
z = 0
if o =="+":
  z = n + t
  print(f"Result : {z:.2f}")
elif o =="-":
   z = n - t
   print(f"Result : {z:.2f}")
elif o =="*":
    z = n * t
    print(f"Result : {z:.2f}")
elif o =="/":
    if t == 0:
         print("Cannot divide by zero")
    else:
         z = n / t
         print(f"Result : {z:.2f}")  
else:
    print("Invalid operator")