w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w/(h**2)
if bmi >= 0:
    if bmi < 18.5:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Underweight")
        
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Normal weight")
    elif 25 <= bmi < 30:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Overweight")
    else:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Obese")
else:
    print("Invalid input")