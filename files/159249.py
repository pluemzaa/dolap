w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
if w > 0 or h > 0:
    bmi = w / h**2
    if bmi < 0:
        print("Invalid input")
    elif bmi >= 0 and bmi < 18.5:
             print(f"Your BMI is: {bmi:.2f}")
             print("Category: Underweight")
    elif bmi >= 18.5 and bmi < 25:
             print(f"Your BMI is: {bmi:.2f}")
             print("Category: Normal weight")
    elif bmi >= 25 and bmi < 30:
             print(f"Your BMI is: {bmi:.2f}")
             print("Category: Overweight")
    else:
             print(f"Your BMI is: {bmi:.2f}")
             print("Category: Obese")
else:
     print("Invalid input")