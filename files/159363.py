weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")