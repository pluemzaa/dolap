w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / (h)**2

if bmi > 0:
    print (f"Your BMI is: {bmi:.2f} ")
    if bmi < 18.5:
        print("Category: Underweight")
    if bmi <= 18.5 and bmi < 25:
        print("Category: Normal weight")
    if bmi <= 25 and bmi < 30:
        print("Category: Overweight")
    if bmi >= 30:
        print("Category: obese")
else:
    print("Invalid input")