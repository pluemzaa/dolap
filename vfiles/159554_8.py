weight = int(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))

if weight <= 0 or height <= 0:
    print("Invalid input")
if weight > 0 and height > 0:
   BMI = weight / (height * height)
   print(f"Your BMI is: {BMI:.2f}")
   if BMI < 18.5 :
       print("Category: Underweight")
   elif 18.5 <= BMI < 25:
       print("Category: Normal weight")
   elif 25 <= BMI < 30:
       print("Category Overweight")
   elif BMI >= 30:
       print("Category: Obese")  
else:
    print("Category: Obese")