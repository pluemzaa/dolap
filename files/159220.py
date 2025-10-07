w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
if w >= 0 and h >= 0:
    bmi = w / (h**2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight") 
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")