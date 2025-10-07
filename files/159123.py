a = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
u = (input("Enter the operator (+, -, *, /): "))

if u == "+":
      A1 = a+n
      print(f"Result : {A1:.2f}")
elif u == "-":
      A2 = a-n
      print(f"Result : {A2:.2f}")
elif u == "*":
      A3 = a*n
      print(f"Result : {A3:.2f}")
elif u == "/":
      if n > 0:
            A4 = a/n
            print(f"Result : {A4:.2f}")
      else:
            print("Cannot divide by zero")
else:
      print('Invalid operator')