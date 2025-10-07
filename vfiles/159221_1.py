w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/(h**2)
if w > 0 or h > 0:
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        Category = ("Underweight")
        print(f"Category: {Category}")
    elif BMI < 25:
        Category = ("Normal weight")
        print(f"Category: {Category}")
    elif BMI < 30:
        Category = ("Overweight")
        print(f"Category: {Category}")
    else:
        Category = ("Obese")
        print(f"Category: {Category}")
else:
    print("Invalid input")