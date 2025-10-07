w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/(h**2)

if BMI > 0 and BMI < 18.5:
   print("Your BMI is: %.2f"% (BMI))
   print("Category: Underweight")
if BMI >= 18.5 and BMI < 25:
   print("Your BMI is: %.2f"% (BMI))
   print("Category: Normal weight")
elif BMI >= 25 and BMI < 30:   
   print("Your BMI is: %.2f"% (BMI))
   print("Category: Overweight")
elif BMI >= 30 :
   print("Your BMI is: %.2f"% (BMI))
   print("Category: Obese")
else:
   print("Invalid input")