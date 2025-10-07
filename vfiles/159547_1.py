w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w/h**2
print(f"Your BMI is: {bmi:.2f}")
if w <= 0 and h <= 0:
    print("Invalid input")
if bmi < 18.5:
    c =("Underweight")
elif bmi <= 18.5 and bmi < 25:
    c =("Normal Weight")
elif bmi <= 25 and bmi < 30:
    c =("Overweight")
elif bmi >= 30:
    c =("Obese")
print(f"Category: {c}")