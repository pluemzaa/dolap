w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI=0
if w > 0 and h > 0:
  BMI = w / (h*h)
  print(f"Your BMI is: {BMI:.2f}")

  if BMI < 18.5:
    print ("Category : Underweight")
  elif BMI < 25:
    print ("Category : Normal weight")
  elif BMI < 30:
    print ("Category: Overweight")
  else:
    print("category: Obese")
else :
    print ("Invalid input")