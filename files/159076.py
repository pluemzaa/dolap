weight = int(input("Enter your  weight (kg): "))
height = float(input("Enter your  height (m): "))
b = weight / (height)**2
if b >= 0:
      if b < 18.5:
         print(f"Your BMI is: {b:.2f}")
         print("Category:Underweight")
      elif b >= 18.5 and b < 25:
         print(f"Your BMI is: {b:.2f}")
         print("Category:Normal weight")
      elif b >= 25 and b < 30:
        print(f"Your BMI is: {b:.2f}")
        print("Category:Overweight")
      
      else:
          print(f"Your BMI is: {b:.2f}")
          print("Category:Obese")
else:
    print("Invalid input")