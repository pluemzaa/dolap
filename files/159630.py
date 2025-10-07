w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / (h ** 2)

if w <= 0 or h <= 0:
    print("Invalid input")
else:
    if bmi < 18.5:
        c = "Underweight"
    elif bmi < 25:
        c = "Normal Weight"
    elif bmi < 30:
        c = "Overweight"
    else:
        c = "Obese"
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {c}")