w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w/h**2
if w <= 0 or h <= 0:
    print("Invalid input")
#print(f"Your BMI is: {bmi:.2f}")
else:
    if bmi < 18.5:
        c =("Underweight")
    elif bmi <= 18.5 and bmi < 25:
        c =("Normal Weight")
    elif bmi <= 25 and bmi < 30:
        c =("Overweight")
    elif bmi >= 30:
        c =("Obese")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {c}")