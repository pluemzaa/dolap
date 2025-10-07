w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
Bmi = w / h**2
if w > 0 and h > 0:
    if Bmi < 18.5:
       x = "Underweight"
    elif Bmi < 25:
       x = "Normal weight"
    elif Bmi < 30:
       x = "Overweight"
    else:
       x = "Obese"
    print(f"Your BMI is: {Bmi:.2f}")
    print("Category:", x)
else:
    print("invalid input")