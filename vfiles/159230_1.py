weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
BMI = weight/height**2

if BMI > 0:
        print("Your BMI is:",BMI)
elif 18.5 <= BMI < 25:
    print("Category: Normal weight")
elif 125 <= BMI < 30:
    print("Category: Overweight")
elif BMI >= 30:
    print("Category: Obese")
elif weight <= 0:
    print("Invalid input")
else:
    print("Invalid input")