w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/h**2
if BMI > 0:
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("Category: Underweight")
    if 18.5 <= BMI < 25:
        print("Category: Normal weight")
    if 25 <= BMI < 30:
        print("Category: Overweight")
    if BMI >= 30:
        print("Category: Obese")
else:
    print("Invalid input")