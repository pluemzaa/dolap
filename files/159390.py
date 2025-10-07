w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/h**2
if w < 0:
    print("Invalid input")
elif BMI < 18.5:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category : Underweight")
elif BMI < 25:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category :Normal weight")
elif BMI < 30:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category :Overweight")
elif BMI >= 30:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category :Obese")
else:
    print("Invalid input")