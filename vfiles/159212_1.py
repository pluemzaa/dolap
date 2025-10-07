w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/(h**2)

if w > 0 and h > 0:
    if BMI < 18.5:
        a = "Underweight"
    elif BMI < 25:
        a = "Normal weight"
    elif BMI < 30:
        a = "Overweight"
    else:
        a = "Obese"
    print(f"Your BMI is: {BMI:.2f}")
    print(f"Category: {a}")
else:
    print("Invalid input")