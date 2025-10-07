x1 = int(input("Enter the first number: "))
x2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
sum = 0
if op == "+" :
  sum = x1+x2
  print(f"Result : {sum:.2f}")
elif op == "-":
  sum = x1-x2
  print(f"Result : {sum:.2f}")
elif op == "*":
  sum = x1*x2
  print(f"Result : {sum:.2f}")
elif op == "/" :
  if x2 > 0 :
    sum = x1/x2
    print(f"Result : {sum:.2f}")
  else :
    print("Cannot divide by zero")
else :
  print("Invalid operator")