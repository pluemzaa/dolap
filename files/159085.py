w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

if w > 0 and h > 0:
    BMI = w/(h)**2
    if BMI < 18.5:
      c = "Underweight"
    elif BMI >= 18.5  and BMI <= 25:
      c = "Normal weight"
    elif BMI >= 25 and BMI <= 30:
      c = "Overweight"
    else:
      c = "Obese"
    print(f"Your BMI is:{BMI:.2f}")
    print(f"Category: {c}")
else:
    print("Invalid input")