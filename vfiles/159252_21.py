w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

bmi = w / (h**2)

if h > 0 and w > 0:
    print(f"Your BMI is: {bmi:.2f}")
    if bmi > 18.5 and bmi <= 30:
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi >= 18.5 and bmi < 25:
            print("Category: Normal weight")
        elif bmi >= 25 and bmi < 30 :
            print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")