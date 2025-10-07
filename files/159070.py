w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

if w > 0 and h > 0:
    bmi = w / (h ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
else:
    print("Invalid input")