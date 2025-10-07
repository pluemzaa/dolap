w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/(h**2)
if w <= 0 or h <= 0:
    print("Invalid input")
elif BMI < 18.5 :
    Category = ("Underweight")
elif 18.5 <= BMI < 25:
    Category = ("Normal weight")
elif 25 <= BMI < 30:
    Category = ("Overweight")
elif BMI >= 30:
    Category = ("Obese")
print(f"Your BMI is: {BMI:.2f}")
print(f"Category: {Category}")