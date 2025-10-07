w = float(input('Enter your weight (kg):'))
h = float(input('Enter your height (m):'))
bmi = w/h**2
if bmi > 0:
    if bmi < 18.5:
        category = ("Underweight")
    elif bmi < 25:
        category = ("Normal weight")
    elif bmi < 30:
        category = ("Overweight")
    else:
        category= ("Obese")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
else:
    print("Invalid input")