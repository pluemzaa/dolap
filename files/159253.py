weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
BMI = weight  / (height)**2
if BMI >0 :
    print(f"Your BMI is: {BMI:.2f}")
if BMI >0 and BMI < 18.5 :
    print("Category: Underweight")
if BMI >= 18.5 and BMI < 25 :
    print("Category: Normal weight")
if BMI >= 25 and BMI < 30 :
    print("Category: Overweight")
if BMI >= 30 :
    print("Category: Obese")
else:
    print("Invalid input")