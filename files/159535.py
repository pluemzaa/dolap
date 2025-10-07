num1 = float(input("Enter the first number:  "))
num2 = float(input ("Enter the second number: "))
operator = input("Enter the operator (+, -, *,/): "))
if operator is '+' : 
  print("Result :%.2f" % (num1 + num2))
elif operator is '-'
  print ("Result :%.2f" % (num1 - num2))
elif operator is '*':
  print ("Result :%.2f" % (num1 * num2))
elif operator is '/'
  if num2 == 0
     print("Cannot divide by zero")
else:
     print("Result:%.2"(num1/num2))
else:
  print("Invalid operator")