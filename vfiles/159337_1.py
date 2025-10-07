weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
BMI = 0

if weight > 0 and height > 0:
    BMI = weight / (height * height)
    print(f"Your BMI is: {BMI:.2f}")

    if BMI < 18.5:
      print(" Category: Underweight" )
    elif BMI < 25: 
      print("Category:  Normal weight")
    elif BMI < 30:
      print("Category: Overweight")
    elif BMI >= 30:
      print("Category :Obese")