x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = input("Enter the operator (+, -, *, /):")
if z == "+":
 print(f"Result : {x+y:.2f} ")
elif z == "-":
     print(f"Result : {x-y:.2f} ")
elif z == "*":
     print(f"Result : {x*y:.2f} ")
elif z == "/": 
      if y == 0 :
       print ("Cannot divide by zero")
      else:
       print(f"Result : {x/y:.2f} ")             
else :
    print("Invalid operator")