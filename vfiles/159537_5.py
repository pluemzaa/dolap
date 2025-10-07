we = float(input("Enter your weight (kg): "))
wi = float(input("Enter your height (m): "))

BMI = we / ((wi)**2)
if we >= 0 or wi >= 0:
    if BMI >= 30:
        print(f"Your BMI is: {BMI:.2f}")
        print("Category: Obese")
    elif BMI < 18.5:
        print(f"Your BMI is: {BMI:.2f}")
        print("Category: Underweight")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI is: {BMI:.2f}")
        print("Category: Normal weight")
    elif 25 <= BMI < 30:
        print(f"Your BMI is: {BMI:.2f}")
        print("Category: Overweight")
else:
    print("Invalid input")